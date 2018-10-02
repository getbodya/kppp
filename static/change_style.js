function change_style(){
    var ui_style = $('#change_style').attr('name')
    var uis = String(ui_style)
    console.log(uis)

    $.ajax({
        type: "GET",
        url:  "../../change_style/",
        data:{
        'ui_style': uis,
        },
        dataType: "text",
        success: function(html){
              }
  })
}
