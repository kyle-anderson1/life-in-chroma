  function whoShow(){
    who.innerHTML = "<h1 id='aH'>Who We Are!</h1>" +
    "<p id='aP'>Karan and Kyle are both computer science students at Tufts University." +
    " We built this project on the Google App Engine with Python using Jinja2." +
    " All the HTML, CSS, and JavaScript was developed by us and the Python we learned" +
    " from our Cloud Applications course and <strong>Programming Google App Engine with Python</strong>" +
    " by Dan Sanderson.</p>" + "<button id='aB' onclick='whoUnshow()'>Show Less</button>";
    who.style.background = "#66b3ff";
    h1 = document.getElementById("aH");
    p = document.getElementById("aP");
    b = document.getElementById("aB");
    h1.style.textAlign = "center";
    h1.style.color = "white";
    p.style.fontSize = "1rem";
    p.style.padding = "15px";
    p.style.color = "white";
    b.style.fontFamily = "Josefin Slab";
    b.style.fontSize = "1.5rem";
    b.style.color = "white";
    b.style.position = "relative";
  }
  function whoUnshow(){
    who.innerHTML = "<button onclick='whoShow()'>Who We Are!</button>";
    who.style.background = "url('https://static.pexels.com/photos/458555/pexels-photo-458555.jpeg')";
    who.style.backgroundSize = "cover";
  }

  function whatShow(){
    what.innerHTML = "<h1 id='aH'>What We Do!</h1>" +
    "<p id='aP'>" +
    "This web application will produce beautiful albums given a collection of images from your library." +
    " Features include being able to manage your albums, share them with your friends, and" +
    " eventually put them into a themed slide show." +
    "</p>" +
    "<button id='aB' onclick='whatUnshow()'>Show Less</button>";
    what.style.background = "#66b3ff";
    h1 = document.getElementById("aH");
    p = document.getElementById("aP");
    b = document.getElementById("aB");
    h1.style.textAlign = "center";
    h1.style.color = "white";
    p.style.fontSize = "1rem";
    p.style.padding = "15px";
    p.style.color = "white";
    b.style.fontFamily = "Josefin Slab";
    b.style.fontSize = "1.5rem";
    b.style.color = "white";
    b.style.position = "relative";
  }
  function whatUnshow(){
    what.innerHTML = "<button onclick='whatShow()'>What We Do!</button>";
    what.style.background = "url('https://static.pexels.com/photos/208701/pexels-photo-208701.jpeg')";
    what.style.backgroundSize = "cover";
  }
