document.addEventListener("DOMContentLoaded", (e)=> {
	var item=document.getElementsByClassName("item");

	
	for (var i = 0; i<item.length;i++) {
		item[i].addEventListener("click",function () {setHighlite(this);},false);
	}

	function setHighlite (e) {

	}

});	