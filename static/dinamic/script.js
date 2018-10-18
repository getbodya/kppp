
window.onload = function() {
    var btnInput = document.getElementById('btn')
    btnInput.addEventListener('click',clicker);
}

function clicker(){
    var el = document.getElementById("input")
dynamics.animate(el, {
    translateX:1000,
    scale: 1,
    opacity: 0
  }, {
    type: dynamics.liner,
    duration: 100,
  })
}