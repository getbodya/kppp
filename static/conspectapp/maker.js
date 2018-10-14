function maker(){
  var name = $('#name').val()
  var description = $('#description').val()
  var specialty = $('#specialty').val()
  var content = $('#conspect').val()
  var tags = $('#tags').val()
  console.log(name)
  console.log(description)
  console.log(specialty)
  console.log(content)

  $.ajax({
    type: "GET",
    url:  "/userpage/make_conspect/",
    data:{
      'name' : name,
      'description': description,
      'specialty': specialty,
      'content': content,
      'tags': tags,
    },
    dataType: "text",
    success: function(html){  
                  $('#mkconspect').html(html);  
              }  
  })
  }
