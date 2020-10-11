$( document ).ready(function() {
    console.log( "ready!" );

    $("#searchProducts").click(function(){
        $("#extendedSearchBar").toggle();
    });
});