# -*- coding: utf-8 -*-
import pjsua as pj
import threading,os,time
import re

def log_cb(level, str, len):
    #if level >= 2:
    #print str
    return 
    
class DefaultAccountCB(pj.AccountCallback):
    sem=None
    def __init__(self,account=None,callcallback=None,sipclient=None):
        pj.AccountCallback.__init__(self, account=None)
        self.callcallback=callcallback
        self.sc=sipclient
    def wait(self):
        self.sem =threading.Semaphore(0)
        for i in range(10):
            if self.sem.acquire(blocking=False) or self.account.info().reg_status==200:
                return True
            time.sleep(1)
        return False
    def on_reg_state(self):
        if self.sem:
            if self.account.info().reg_status==200:
                self.sem.release()
        self.sc.reg_status=self.account.info().reg_status
    
    def on_incoming_call(self,call):
        call_cb=self.callcallback if self.callcallback else DefaultCallCallback(call,sipclient=self.sc)
        call.set_callback(call_cb)
        call.answer(180)
        #call.answer(200)
        self.sc.ringing_call=call
        
class DefaultCallCallback(pj.CallCallback):
    def __init__(self, call=None,sipclient=None):
        pj.CallCallback.__init__(self, call)
        self.sc=sipclient
    def on_state(self):
        if self.call.info().state==pj.CallState.DISCONNECTED:
            self.sc.current_call=None
            
    def on_media_state(self):
        if self.call.info().media_state==pj.MediaState.ACTIVE:
            call_slot = self.call.info().conf_slot
            lib=pj.Lib.instance()
            lib.conf_connect(call_slot,0)
            lib.conf_connect(0,call_slot)
            self.sc.player.play('phone1.wav',True,call_slot,True)
            
class Player:
    def __init__(self,filename=None,lib=None):
        self.player_id=-1
        self.player_slot=-1
        self.filename=filename
        self.created={}
        if lib:
            self.lib=lib
        elif pj.Lib.instance():
            self.lib=pj.Lib.instance()
        else:
            self.lib = pj.Lib()
            self.lib.init(log_cfg = pj.LogConfig(level=2,callback=log_cb))
            self.lib.start()
        
        
    def play(self,filename=None,oncall=False,call_slot=-1,loop=False):
        if not filename and not self.filename:
            return -1 #没有指定播放文件
        if filename:
            if os.path.exists(filename):
                self.tmpfile=filename
            else:
                return -2 #播放文件不存在
        else:
            if os.path.exists(self.filename):
                self.tmpfile=self.filename
            else:
                return -2
        if self.tmpfile in self.created.iterkeys():
            slot=self.lib.player_get_slot(self.created[self.tmpfile])
            self.lib.conf_disconnect(slot,0)
            self.lib.player_destroy(self.created[self.tmpfile])
        self.player_id=self.lib.create_player(self.tmpfile,loop=loop)
        self.created[self.tmpfile]=self.player_id
        self.player_slot=self.lib.player_get_slot(self.player_id)
        if not oncall:
            self.lib.conf_connect(self.player_slot,0)
        else:
            self.lib.conf_connect(self.player_slot,call_slot)
            self.lib.conf_connect(call_slot,self.player_slot)
        
    def stop(self,oncall=False,slot=-1):
        dstslot=slot if oncall else 0
        try:
            self.lib.conf_disconnect(self.player_slot,dstslot)
            self.player_destroy(self.created[self.tmpfile])
            del self.created[self.tmpfile]
        except:
            pass

                     
class SipClient():
    reg_status=None
    current_call=None
    ringing_call=None
    tmpacc=None
    def __init__(self,lib=None):
        if lib:
            self.lib=lib
        elif pj.Lib.instance():
            self.lib=pj.Lib.instance()
        else:
            self.lib = pj.Lib()
            ua=pj.UAConfig()
            ua.max_calls=40
            self.lib.init(log_cfg = pj.LogConfig(level=2,callback=log_cb),ua_cfg=ua)  
            self._transport=self.lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(0))
            self.lib.start()  
        devs=self.lib.enum_snd_dev()
        if not len(devs):
            self.lib.set_null_snd_dev()
        self.player=Player()
        self.created={}
        
    def register(self,extern,host,port=5060,password=None,renew=True,tmp=True):
        if not password:
            password=extern
        sip='sip:%s@%s:%s'%(extern,host,port)
        domain="%s:%s"%(host,port)
        if self.created.has_key(sip):
            self.created[sip].set_registration(renew)
            return self.created[sip]
        if (tmp and not self.tmpacc) or not tmp:
            acc=self.lib.create_account(pj.AccountConfig(domain=domain,username=extern,password=password),set_default=False)
            acc_cb=DefaultAccountCB(acc,sipclient=self)
            acc.set_callback(acc_cb)
            if not acc_cb.wait():
                return None
            if tmp:
                self.tmpacc=acc
            else:
                self.created[sip]=acc
            return acc
        if tmp and self.tmpacc:
            #self.tmpacc.set_registration(False)
            acc_id=self.tmpacc._id
            self.lib.modify_account(acc_id,pj.AccountConfig(domain=domain,username=extern,password=password))
            #if not self.tmpacc._cb.wait():
            #    return None
            #self.tmpacc.set_registration(renew)
            return self.tmpacc
    
    def modifyacc(self,old_uri,new_uri):
        if not old_uri in self.created.iterkeys():
            return None
        acc_id=self.created[old_uri]._id
        
        uri=pj.SIPUri(new_uri)
        domain=uri.host
        if uri.port==0:
            domain="%s:5060"%domain
        else:
            domain="%s:%s"%(domain,uri.port)
        extern=uri.user
        password=uri.user
        self.lib.modify_account(acc_id,pj.AccountConfig(domain=domain,username=extern,password=password))
        
    def makecall(self,sipuri,remoteuri,password=None,rpassword=None,callback=None,innercall=True):
        sipuri=pj.SIPUri(sipuri)
        if int(sipuri.port)==0:
            sipuri.port='5060'
        remoteuri=pj.SIPUri(remoteuri)
        if int(remoteuri.port)==0:
            remoteuri.port='5060'
        acc=self.register(sipuri.user,sipuri.host,sipuri.port,password,tmp=True)
        if not acc:
            return False
        if innercall:
            self.register(remoteuri.user,remoteuri.host,remoteuri.port,rpassword)
        cb=callback if callback else DefaultCallCallback(sipclient=self)
        call=acc.make_call(remoteuri.encode(),cb=cb)
        self.current_call=call
        return True
    
    def hangup(self,code=603):
        """if self.current_call:
            self.current_call.hangup(code)
            self.current_call=None
        elif self.ringing_call:
            self.ringing_call.hangup(code)
            self.ringing_call=None"""
        self.lib.hangup_all()
        self.current_call=None
        self.ringing_call=None
        
    def answer(self,code=200,timeout=10):
        for i in range(timeout):
            if self.ringing_call:
                self.ringing_call.answer(code)
                self.ringing_call=None
                print 'call answered!'
                break
            time.sleep(1)
                

    def dtmf(self,digits):
        if not re.match(r'^[\d#*]+$',digits):
            print 'The dtmf digits is not correct!'
            return
        if self.current_call:
            self.current_call.dial_dtmf(digits)
        else:
            print 'There is no call!'
        
    def unregister(self):
        for acc in self.created.itervalues():
            acc.set_registration(False)
        if self.tmpacc:
            self.tmpacc.set_registration(False)
            self.tmpacc.delete()
            self.tmpacc=None
    
    def clear(self):
        self.hangup()
        for sip in self.created.iterkeys():
            self.deleteacc(sip)
        if self.tmpacc:
            self.tmpacc.set_registration(False)
            self.tmpacc.delete()
            self.tmpacc=None
            
    def deleteacc(self,uri):
        if uri in self.created.iterkeys():
            acc=self.created[uri]
            del self.created[uri]
            acc.delete()
            del acc
    
    
        
    """SIPUri.encode有bug,需修改pjsua.py 674行为 output = output + ":" + str(self.port) """
if __name__=='__main__':
    sc=SipClient()
    sc.register('200','192.168.18.114',tmp=False)
    sc.register('201','192.168.18.114',tmp=False)
    sc.register('202','192.168.18.114',tmp=False)
    sc.register('203','192.168.18.114',tmp=False)
    sc.register('204','192.168.18.114',tmp=False)
    sc.register('205','192.168.18.114',tmp=False)
    sc.register('206','192.168.18.114',tmp=False)
    #sc.deleteacc('sip:201@192.168.18.114:5060')
    #sc.deleteacc('sip:202@192.168.18.114:5060')
    sc.register('207','192.168.18.114',tmp=False)
    sc.register('208','192.168.18.114',tmp=False)
    sc.register('209','192.168.18.114',tmp=False)
    sc.register('210','192.168.18.114',tmp=False)
    sc.makecall('sip:13421344506@192.168.18.191','sip:55550114@192.168.18.114',innercall=False)
    sc.player.play('phone1.wav',loop=True)
    time.sleep(2)
    sc.dtmf('200')
    time.sleep(4)
    sc.answer()
    time.sleep(20)
    sc.hangup()"""
  #  sc.unregister()
    while True:
        time.sleep(1)
        break    
