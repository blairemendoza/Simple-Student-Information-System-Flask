/* Timer function for alerts */
window.setTimeout(function() {
    $('#flash').fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 5000);