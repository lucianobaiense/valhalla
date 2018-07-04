function handlerFocus(event){
    var item = event.target;
    var itemParent = item.parentNode;
    var label = itemParent.querySelector('label');
    label.classList.add('green');
    item.classList.add('green');

}
function handlerBlur(event){
    var item = event.target;
    value = item.value;
    var itemParent = item.parentNode;
    var label = itemParent.querySelector('label');

    if(value === ""){
        label.classList.remove('green');
        item.classList.remove('green');
    }

}

(function(){

    var inputs = document.querySelectorAll('input[data-type="form-input"],textarea');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('focus', handlerFocus.bind());
        inputs[i].addEventListener('focusout', handlerBlur.bind());
        console.log(inputs[i].value);
        if(inputs[i].value){

            var inputParent = inputs[i].parentNode;
            var label = inputParent.querySelector('label');

            inputs[i].classList.add('green');
            label.classList.add('green');
        }
    }



})();
