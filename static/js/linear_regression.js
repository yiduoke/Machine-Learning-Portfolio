var fs = require('fs');

  if (fs.exists('scripts-ex1/plot.jpg') == true) {      
    console.log('fs exists');		  
	} else {
	  console.log('Not Found!');   
	}		       

// function recursively_ajax(){
//   console.log("begin");
//   $.get("scripts-ex1/plot.jpg")
//   .done(
//     function() {
//       results.setAttribute("src", "scripts-ex1/plot.jpg"); 
//     }
//   )
//   .fail(
//     function() {
//       recursively_ajax();
//     }
//   )
// }

// recursively_ajax();