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

const videoDropdown = document.getElementById('videoDropdown');
const submitBtn = document.getElementById('submitBtn');

        
submitBtn.addEventListener('click', function() {
    const selectedVideo = videoDropdown.value;
           
    fetch('/process_selected_video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ video: selectedVideo })
    })
    .then(response => response.json())
    .then(data => {

    console.log(data);
})
.catch(error => {
    console.error('Error:', error);
});
});