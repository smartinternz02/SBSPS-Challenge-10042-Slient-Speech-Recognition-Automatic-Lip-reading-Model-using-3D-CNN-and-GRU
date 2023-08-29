const menu = document.querySelector(".menu");
const menuList = document.querySelector("nav ul");

const pred = document.getElementById('prediction');


document.getElementById('videoDropdown').addEventListener('change', function() {
  var video = document.getElementById('video');
  var source = document.getElementById('videoSource');
  source.src = "static/data/s1/" + this.value;
  console.log(this.value);
  console.log(source.src); 
  video.load();
});

var video = document.getElementById('video')
var source = document.getElementById('videoSource');
console.log(source.src);  

const submitBtn = document.getElementById('submitBtn');
const videoDropdown = document.getElementById('videoDropdown');
videoDropdown.addEventListener('change', function() {
  pred.textContent = "";
})

function changeColor(){
  const predicto= document.getElementById("prediction");
  predicto.classList.remove("dark:text-gray-500");
  predicto.classList.add("dark:text-slate-300");
  const actualo= document.getElementById("actual");
  actualo.classList.remove("dark:text-gray-500");
  actualo.classList.add("dark:text-slate-300");
}

// function loadMoreInfo(){
//     var url = "http://www.apple.com";
//     window.location.href = url;
// }