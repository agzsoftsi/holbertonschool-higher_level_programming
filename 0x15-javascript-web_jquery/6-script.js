/* Task 6 - script that updates the text of the HTML tag HEADER to "New Header!!!" when the user clicks on DIV#update_header
You must use the jQuery API
to Change the text inside the header using replaceWith
*/
$('#update_header').click(function () {
  $('header').replaceWith('New Header!!!<br>');
});
