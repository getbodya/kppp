function geter(){
    var content = $('textarea#conspect').val()
    var conspect_id = $('#conspect').attr('name')

    console.log(content)  
    console.log(conspect_id)  

  $.ajax({
    type: "GET",
    url:  "../../../get_edit_conspect/",
    data:{
      'content' : content,
      'conspect_id': conspect_id, 
    },
    dataType: "text",
    success: function(html){  
                  $('#redaktor').html(html);  
              }  
  })
  }
  