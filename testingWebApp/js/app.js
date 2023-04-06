
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
    let newId = Math.ceil(Math.random() * 1000).toString();
    jsonObj.requestId = newId;
    jsonObj.latentCode = generateRandomLatentCodes();
    websocket.send(JSON.stringify(jsonObj));
}

function generateRandomLatentCodes() {
    const numToGenerate = 3;
    const dimension = 236;

    var newLatentCodes = []
    for (let i = 0; i < numToGenerate; i++) {
        var randomLatentCode = []
        for (let j = 0; j < dimension; j++) {
            randomLatentCode.push(gaussianRandom());
        }
        newLatentCodes.push(randomLatentCode);
    }

    return newLatentCodes;
}

// Standard Normal variate using Box-Muller transform.
// source: https://stackoverflow.com/questions/25582882/javascript-math-random-normal-distribution-gaussian-bell-curve
function gaussianRandom(mean=0, stdev=1) {
    let u = 1 - Math.random(); // Converting [0,1) to (0,1]
    let v = Math.random();
    let z = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
    // Transform to the desired mean and standard deviation:
    return z * stdev + mean;
}