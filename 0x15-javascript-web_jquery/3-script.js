/* Task 3 - script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
use the jQuery API to call div with id red_header
define a click funtion to add the clas red to header and change the color of the header to Red
*/
$('#red_header').click(function () {
  $('header').addClass('red');
});
