var view, upload;
view = document.getElementById("view");
upload = document.getElementById("upload");

window.onload = function showView(){
  view.innerHTML = "<h1 id='aH'>View Your Albums</h1>" +
   "<button id='aB' onclick='unShowView()'>Show Less</button>";
  view.style.background = "black";
  h1 = document.getElementById("aH");
  b = document.getElementById("aB");
  h1.style.textAlign = "center";
  h1.style.color = "white";
  b.style.fontFamily = "Josefin Slab";
  b.style.fontSize = "1.5rem";
  b.style.color = "white";
  b.style.position = "relative";
}
window.onload function unShowView(){
  view.innerHTML = "<button onclick='whoShow()'>View Your Albums</button>";
  view.style.background = "url('https://static.pexels.com/photos/189187/pexels-photo-189187.jpeg')";
  view.style.backgroundSize = "cover";
}

window.onload function showUpload(){
  upload.innerHTML = "<h1 id='aH'>Upload an Album</h1>" +
  "<button id='aB' onclick='whatUnshow()'>Show Less</button>";
  upload.style.background = "black";
  h1 = document.getElementById("aH");
  b = document.getElementById("aB");
  h1.style.textAlign = "center";
  h1.style.color = "white";
  b.style.fontFamily = "Josefin Slab";
  b.style.fontSize = "1.5rem";
  b.style.color = "white";
  b.style.position = "relative";
}
window.onload function showUpload(){
  upload.innerHTML = "<button onclick='whatShow()'>What We Do!</button>";
  upload.style.background = "url('https://static.pexels.com/photos/205385/pexels-photo-205385.jpeg')";
  upload.style.backgroundSize = "cover";
}
