function chooseBtn(btn) {
	btn.isChosen = true;			
	btn.innerHTML = "Убрать из<br>корзины ";
	btn.setAttribute('class', 'add chosen');
}

let buttons = document.querySelectorAll('table > tbody > tr > td > button.add');
for (var i = 0; i < buttons.length; ++i) {
	buttons[i].isChosen = false;
	buttons[i].onclick = function() {
		let ajax = new XMLHttpRequest();
		if (this.isChosen) {
			ajax.open('GET', '../cart/remove?id=' + this.id);

			this.isChosen = false;
			this.innerHTML = "Добавить<br>в корзину";
			this.setAttribute('class', 'add');
		} else {
			ajax.open('GET', '../cart/add?id=' + this.id);
			
			chooseBtn(this);
		}
		ajax.send();
	}
}

let ajax = new XMLHttpRequest();
ajax.open('GET', '../cart/chosen-ids');
ajax.send();
ajax.onload = function() {
	let ids = JSON.parse(this.responseText);
	for (let id of ids) {
		btn = document.getElementById(id);
		chooseBtn(btn);
	}
}