function sends(){
    var messange = $('#text-input').val();
    console.log(message)
    $.ajax({
        type: "GET",
        url: "{% url 'q_and_a' %}",
        data:{
            'messanges': messanges,
        },
        dataType: "text",
        //success: function(data){
          //  $("#chat-field").html(data);
            //    }
        })
}