
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

function generatePointCloudsWithRandomCodes() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    console.log(this.readyState);
    console.log(this.status)
    console.log(this.responseText)
    if (this.readyState == 4 && this.status == 200) {
      var pointClouds = JSON.parse(this.responseText);
      document.getElementById("jsonResult").textContent = JSON.stringify(pointClouds, undefined, 4);
    }
  };

  xhttp.open("POST", "http://127.0.0.1:5000/generateFromLatentCode/yourRequestId", true);
  xhttp.setRequestHeader('Content-type', 'application/json')

  var jsonObj = new Object();
  jsonObj.latentCode = [1,2,3];

  xhttp.send(JSON.stringify(jsonObj));
}

// function generateRandomLatentCode() {
//   const numToGenerate = 3;
//   const dimension = 236;

//   for (let i = 0; i < numToGenerate; i++) {
//     for (let j = 0; j < dimension; j++) {
      
//     }
//   }
// }