function get_rating( ){
  var value =  $("input[type=radio]:checked").attr("value")
  var conspect_id = $('#conspect').attr('name')
  console.log(value)  
  console.log(conspect_id)  
  
  $.ajax({
    type: "GET",
    url:  "../../get_rating/",
    data:{
      'rating' : value,
      'conspect_id': conspect_id, 
    },
    dataType: "text",
    success: function(html){  
                  $('.rating').html(html);  
              }  
  })
}