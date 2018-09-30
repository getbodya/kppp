  $("#check").click(function (){
    $.ajax({
      type: "GET",
      url:  "check_comment/",
      data:{
        "conspect_id":$("#comment_field").val(),
      },
      dataType: "text",
      cache: false,

      success: function(data){}
    })
})


function sss() {
  alert("1");
  
}