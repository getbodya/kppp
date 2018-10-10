function like(cid){
	var like = 'like';
	var comment_id = cid;
	data = {
		comment_id: comment_id,
		like: like
	};
	$.ajax({
		type:"GET",
		url: "../../user_reaction",
		dataType:'json',
		data: data,
		success: function(data){
			$('#liked').html(data.likes)
			}
		})
	}

function dislike(cid){
	var dislike = 'dislike';
	var comment_id = cid;
	console.log(dislike);
	console.log(comment_id);
	data = {
		comment_id: comment_id,
		dislike: dislike
	};
	$.ajax({
		type:"GET",
		url: "../../user_reaction",
		dataType:'json',
		data: data,
		success: function(data){
			$('#disliked').html(data.dislikes)
			}
		})
	}	