console.log("Liberal Arts Website Loaded");

window.onload = function(){

alert("Welcome to Liberal Arts Department");

}
function darkMode(){
document.body.classList.toggle("dark");
}


function animateValue(id, start, end, duration) {

let obj = document.getElementById(id);
let range = end - start;
let current = start;
let increment = 1;
let stepTime = Math.abs(Math.floor(duration / range));

let timer = setInterval(function() {

current += increment;
obj.innerHTML = current;

if (current == end) {
clearInterval(timer);
}

}, stepTime);

}

animateValue("studentsCount",0,120,2000);
animateValue("facultyCount",0,15,2000);
animateValue("coursesCount",0,20,2000);
animateValue("placementsCount",0,85,2000);