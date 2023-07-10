document.getElementsByTagName("body")[0].onload=myfunc

function myfunc(argument) {
	let labelelements=document.querySelectorAll("p label")
	for(let x=0;x<labelelements.length;x++){
		labelelements[x].style.fontWeight="bold"
	}
	labelelements[labelelements.length-1].innerHTML="Kateqoriya seç"
	labelelements[2].innerHTML="Məzmun"
	document.querySelector("p>label").setAttribute("class","form-label")
	document.getElementById("id_image").setAttribute('class','form-control mb-3')
	document.getElementById("id_titleofblog").setAttribute('class','form-control mb-3')
	document.querySelector("p>select").setAttribute('class','form-select')
	document.querySelector("input[type='submit']").setAttribute('class','btn btn-primary')
}