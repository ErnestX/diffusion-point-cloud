
const websocket  = new WebSocket("ws://localhost:8001/");    
websocket.addEventListener("message", ({ data }) => {
    console.log("received a message");
    let response = JSON.parse(data);
    let rid = response.requestId;
    document.getElementById("IdFromResponse").textContent = rid
    let latentCodes = response.latentCodes;
    document.getElementById("jsonLatentCodeFromResponse").textContent = JSON.stringify(latentCodes, undefined, 4);
    let pointClouds = response.pointClouds
    document.getElementById("jsonPointCloudsFromResponse").textContent = JSON.stringify(pointClouds, undefined, 4);
});
console.log("done Setup");

$(document).ready(function(){
    console.log("document ready");
});

function generatePointCloudsWithRandomCodes(){
    var jsonObj = new Object();
    jsonObj.latentCode = [1,2,3];
    websocket.send(JSON.stringify(jsonObj));
}

    