document.addEventListener('DOMContentLoaded',function(){
	
	if (document.querySelector('#follow')) {
		document.querySelector('#follow').addEventListener('click',()=>follow());
	}
	else if(document.querySelector('#unfollow')){
		document.querySelector('#unfollow').addEventListener('click',()=>unfollow());
	}
	

	function follow(){
		var pathArray = window.location.pathname.split('/');
		var name = pathArray[2];
		fetch(`/follow/${name}`)
		.then(location.reload());
}

function unfollow(){
	var pathArray = window.location.pathname.split('/');
		var name = pathArray[2];
		fetch(`/unfollow/${name}`)
		.then(location.reload());;
}



	});

function hide_post(post){
		document.querySelector(`#content-${post.dataset.id}`).style.display = 'none';

	const form = document.createElement('form');
	form.className = 'form-hide';
	const div = document.createElement('div');
	div.className = 'input-group';
	const span = document.createElement('span');
	span.className = 'input-group-text';
	span.innerHTML = 'Edit Post';
	const textarea = document.createElement('textarea');
	textarea.className = 'form-control';
	textarea.setAttribute('id',`textarea-${post.dataset.id}`);
	textarea.innerHTML = document.querySelector(`#value-${post.dataset.id}`).innerHTML;
	const button = document.createElement('button');
	button.className = 'btn btn-primary';
	button.innerHTML = 'Save';
	button.setAttribute('id','tohide');
	button.setAttribute('type','button');
	button.setAttribute('data-postid',`${post.dataset.id}`);
	div.append(span,textarea);
	form.append(div,button);
	document.querySelector(`#post-${post.dataset.id}`).append(form);

	if(document.querySelector('#tohide'))
{
	
	document.querySelector('#tohide').addEventListener('click',function(){edit(this)});
}
function edit(edited){
	var block = document.querySelector(`#content-${post.dataset.id}`)
	
	if(document.querySelector(`#textarea-${edited.dataset.postid}`)){
		
		fetch(`/edit/${post.dataset.id}`,{
			method: 'POST',
			body: JSON.stringify({
				content: document.querySelector(`#textarea-${edited.dataset.postid}`).value
			})
		})
		.then(response=>response.json())
		
		.catch(error=>{
			alert(error);
		});
	const cont = document.querySelector(`#textarea-${edited.dataset.postid}`).value;
	document.querySelector(`#content-${post.dataset.id}`).style.display = 'block';
	document.querySelector(`#value-${post.dataset.id}`).innerHTML = `${cont}`;
	


		 if (document.querySelector('.form-hide')){
   var e = document.querySelector('.form-hide');
  var child = e.lastElementChild;
  while(child){
    e.removeChild(child);
    child = e.lastElementChild;
  }
  e.remove(); 
  }
	}
}

}
	

function liked(post){

	if(document.querySelector(`#button-${post.dataset.postid}`).innerHTML === "Like")
	{
var likes = document.querySelector(`#like-${post.dataset.postid}`).innerHTML;
		likes++;
		document.querySelector(`#like-${post.dataset.postid}`).innerHTML = likes;
		document.querySelector(`#button-${post.dataset.postid}`).innerHTML = "Unlike";
		fetch(`like/${post.dataset.postid}`)
	.catch(error=>{
			alert(error);
		});


	}
	else{
		var likes = document.querySelector(`#like-${post.dataset.postid}`).innerHTML;
		likes--;
		document.querySelector(`#like-${post.dataset.postid}`).innerHTML = likes;
		document.querySelector(`#button-${post.dataset.postid}`).innerHTML = "Like";
		fetch(`unlike/${post.dataset.postid}`)
	.catch(error=>{
			alert(error);
		});


	}
		
	
	}

