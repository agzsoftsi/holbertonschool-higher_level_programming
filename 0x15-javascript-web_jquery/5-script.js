/* Task 5 - script that adds a LI element to a list when the user clicks on the tag DIV#add_item
The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
*/
$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
