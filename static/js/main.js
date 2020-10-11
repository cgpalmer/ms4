$( document ).ready(function() {
    console.log( "ready!" );

    $("#searchProducts").click(function(){
        $("#extendedSearchBar").toggle();
    });

    $("#desktopNavAllSearch").click(function(){
        $("#desktopExtendedSearchBar").toggle();
    });

     $("#desktopExtraNavWrapper").hover(function(){
        $("#desktopDropDownMenu").css('display', 'flex');}
        ,function(){
    $("#desktopDropDownMenu").css('display', 'none');
    });

});