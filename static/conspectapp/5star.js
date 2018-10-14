function get_rating(vote){
  var value =  vote
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
                  $('#rat-fil').html(html);  
              }  
  })
}
$(':radio').change(
  function(){
    $('.choice').text( this.value + ' stars' );
  } 
)