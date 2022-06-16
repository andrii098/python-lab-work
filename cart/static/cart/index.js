let btnRemove = document.getElementById("removeAll")
if (btnRemove) {
	btnRemove.onclick = function() {
		let ajax = new XMLHttpRequest();
		ajax.open('GET', './remove-all');
		ajax.send();
		ajax.onload = function() {
			location.replace('../shop');
		}
	}
}