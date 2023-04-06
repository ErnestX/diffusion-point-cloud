$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});

function getExamplePointClouds() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    console.log(this.readyState);
    console.log(this.status)
    if (this.readyState == 4 && this.status == 200) {
      // document.getElementById("demo").innerHTML = this.responseText;
     console.log("success!!");
     alert("success!!!");
  }
};
  xhttp.open("GET", "http://127.0.0.1:5000/generateExamplePointClouds", true);
  xhttp.send();
}