
function show(menu){
    var content = document.querySelectorAll('.tabs-content');
    var menus = document.querySelectorAll('[data-menu]');
    for (var i = 0; i < content.length; i++) {
        content[i].classList.remove('active-content');
        menus[i].classList.remove('active-tab');
    }
    var currentContent = document.querySelector('[data-content="'+menu+'"]');
    var currentMenu = document.querySelector('[data-menu="'+menu+'"]');
    currentContent.classList.add('active-content');
    currentMenu.classList.add('active-tab');
}
(function(){
    var menu = document.querySelector('[data-type="tabs-menu"]');
    menu.addEventListener('click',function(e){
        e.preventDefault();
        if(e.target.nodeName === "A"){
            show(e.target.dataset.menu);
        }
    })

    show('news')
})();
