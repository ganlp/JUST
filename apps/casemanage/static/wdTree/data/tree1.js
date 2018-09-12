function createNode(){ 
    var first=[]
    var file=[] //用例所属文件
    var second=[]  //二级目录
    for(var i=0;i<20;i++){           
      second[i]=[]
      file[i]=[]
    }
    var cases=[]  //用例
    var cases_id=[]
    for(var i=0;i<20;i++){
      cases[i]=[]
      cases_id[i]=[]
      for(var j=0;j<100;j++){
        cases[i][j]=[]
        cases_id[i][j]=[]
      }           
    }
    $.ajaxSettings.async=false;   //设置同步执行的关键----否则必须弹窗后才能加载树形目录
    $.getJSON("/static/wdTree/data/case_name.json",function(data){
        $.each(data,function(i,item){ 
            first.push(item.firstclass)
            console.log(i)
            for(var j=0;j<item.secondclass.length;j++){
              file[i][j]=item.secondclass[j].file
              console.log(file[i])
              second[i].push(item.secondclass[j].name)
              for(var k=0;k<item.secondclass[j].case.length;k++){
                cases[i][j].push(item.secondclass[j].case[k].name)
                cases_id[i][j].push(item.secondclass[j].case[k].id)
                console.log(item.secondclass[j].case[k].name)
              }
            }
          }) 
    })
    $.ajaxSettings.async=true;  //设置同步执行的关键---恢复异步
    var root = {
      "id" : "1",
      "text" : "智能版测试",
      "value" : "智能版测试",
      "showcheck" : true,
      complete : true,
      "isexpand" : true,
      "checkstate" : 0,
      "hasChildren" : true
    };    
  //alert("aaa")
  var arr = [];
  for(var i= 0;i<first.length; i++){
    var subarr = [];
    for(var j=0;j<second[i].length;j++){
      var casearr=[];
      for(var k=0;k<cases[i][j].length;k++){
        var casename=cases[i][j][k];
        var caseid=cases_id[i][j][k];
        casearr.push({
          "id" : "node-"+i+'-'+j+'-'+k,
          "text" : casename,
          "value" : caseid,
          "showcheck" : true,
          complete : true,
          "isexpand" : false,
          "checkstate" : 0,
          "hasChildren" : false
        });
     }
      var value = second[i][j]; 
      subarr.push( {
         "id" : "node-"+i+'-'+j,
         "text" : value,
         "value" : file[i][j],
         "showcheck" : true,
         complete : true,
         "isexpand" : false,
         "checkstate" : 0,
         "hasChildren" : true,
         "ChildNodes": casearr
      })   
    }
    arr.push( {
      "id" : "node-" + i,
      "text" : first[i],
      "value" :"menu",
      "showcheck" : true,
      complete : true,
      "isexpand" : false,
      "checkstate" : 0,
      "hasChildren" : true,
      "ChildNodes" : subarr
    });
  }
  root["ChildNodes"] = arr;
  return root; 
}
treedata = [createNode()];