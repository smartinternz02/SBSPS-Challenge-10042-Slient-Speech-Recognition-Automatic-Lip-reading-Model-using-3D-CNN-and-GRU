const menu = document.querySelector(".menu");
const menuList = document.querySelector("nav ul");
menu.addEventListener("click", () => {
  menuList.classList.toggle("showmenu");
});

document.getElementById('videoDropdown').addEventListener('change', function() {
  var video = document.getElementById('video');
  var source = document.getElementById('videoSource');
  source.src = "static/data/s1/" + this.value;
  console.log(this.value);
  console.log(source.src); 
  video.load();
});

// var video = document.getElementById('video')
// var source = document.getElementById('videoSource');
// console.log(source.src);  