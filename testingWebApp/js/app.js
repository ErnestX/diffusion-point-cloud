function getExamplePointClouds() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    console.log(this.readyState);
    console.log(this.status)
    if (this.readyState == 4 && this.status == 200) {
      var pointClouds = JSON.parse(this.responseText);
      document.getElementById("jsonResult").textContent = JSON.stringify(pointClouds, undefined, 4);
  }
};
  xhttp.open("GET", "http://127.0.0.1:5000/generateExamplePointClouds", true);
  xhttp.send();
}