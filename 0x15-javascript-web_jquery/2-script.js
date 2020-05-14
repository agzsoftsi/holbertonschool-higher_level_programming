/* script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
use the jQuery API to call div with id red_header
define a click funtion to change the color of the header to Red
*/
$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
