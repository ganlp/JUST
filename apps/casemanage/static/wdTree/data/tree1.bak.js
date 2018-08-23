function createNode(){ 
    var first=[]
    var file=[] //用例所属文件
    var second=[]  //二级目录
    for(var i=0;i<20;i++){           
      second[i]=[]   
    }
    var cases=[]  //用例
    for(var i=0;i<20;i++){
      cases[i]=[]
      for(var j=0;j<100;j++){
        cases[i][j]=[]
      }           
    }
    ///static/wdTree/data/casedata.json
    $.getJSON("/static/wdTree/data/case_name.json",function(data){
        $.each(data,function(i,item){ 
            first.push(item.firstclass)
            console.log(i)
            for(var j=0;j<item.secondclass.length;j++){
              file[i]=item.secondclass.file
              second[i].push(item.secondclass[j].name)
              for(var k=0;k<item.secondclass[j].case.length;k++){
                cases[i][j].push(item.secondclass[j].case[k].name)
                console.log(item.secondclass[j].case[k].name)
              }
            }
          }) 
    }) 
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
  alert("aaa")
  var arr = [];
  for(var i= 0;i<first.length; i++){
    var subarr = [];
    for(var j=0;j<second[i].length;j++){
      var casearr=[];
      for(var k=0;k<cases[i][j].length;k++){
        var casename=cases[i][j][k];
        casearr.push({
          "id" : "node-"+i+'-'+j+'-'+k,
          "text" : casename,
          "value" : casename,
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
         "value" : value,
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
      "value" : first[i],
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