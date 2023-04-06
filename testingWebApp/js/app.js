$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});

function getExamplePointClouds() {
  // alert("button pressed");

  // $.get("http://127.0.0.1:5000/generateExamplePointClouds", function(data, status){
  //   alert("success!!!");
  // });

  // Using the core $.ajax() method
  $.ajax({
 
    // The URL for the request
    url: "http://127.0.0.1:5000/generateExamplePointClouds",
 
    // The data to send (will be converted to a query string)
    // data: {
    //     id: "getExamplePointClouds"
    // },
 
    // Whether this is a POST or GET request
    type: "GET",
 
    // The type of data we expect back
    dataType : "application/json",

    success: function(data) {
      console.log("success!!");
      alert("success!!!");
    },

    complete: function(response, textStatus) {
      console.log(response)
      return alert("Hey: " + textStatus);
    }
  });
  // Code to run if the request succeeds (is done);
  // The response is passed to the function
  // .done(function( json ) {
  //   alert("success!!!")
  //   //  $( "<h1>" ).text( json.title ).appendTo( "body" );
  //   //  $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
  // })
  // // Code to run if the request fails; the raw request and
  // // status codes are passed to the function
  // .fail(function( xhr, status, errorThrown ) {
  //   alert( "Sorry, there was a problem!" );
  //   console.log( "Error: " + errorThrown );
  //   console.log( "Status: " + status );
  //   console.dir( xhr );
  // })
  // // Code to run regardless of success or failure;
  // .always(function( xhr, status ) {
  //   alert( "The request is complete!" );
  // });
}