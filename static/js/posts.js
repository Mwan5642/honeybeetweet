////////////////////////////
// JavaScript for Posts page
////////////////////////////

$(function() {
    // Executed when js-menu-icon is clicked
    $('.js-menu-icon').click(function() {
        // $(this) : Self element, namely div.js-meu-icon
        // next() : Next to div.js-menu-icon, namely div.menu
        // toggle() : Switch show and hide
        $(this).next().toggle();
    })
})


///////////////////////////
// JavaScript for Edit Page
///////////////////////////