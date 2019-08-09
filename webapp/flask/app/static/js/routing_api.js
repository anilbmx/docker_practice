function Inserting_doc(e){
  e.preventDefault();
  var url_path = window.location.origin + "/db";
  var fname = $("#fname").val();
  var lname = $("#lname").val();
  var data = {"fname":fname, "lname":lname}
  $.post(url_path, data, function(data){
    console.log(data);
    // data = JSON.parse(data)
    $("#res1").html(data)
  });
}

function Show_all_collection_data(){
  var url_path = window.location.origin + "/db";
  $.get(url_path,function(data){
    console.log(data);
    $("#res2").html(data)
  });
}
