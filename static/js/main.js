$( document ).ready(function() {
    console.log( "ready!" );

    $("#searchProducts").click(function(){
        $("#extendedSearchBar").toggle();
    });



     $("#desktopExtraNavWrapper").hover(function(){
        $("#desktopDropDownMenu").css('display', 'flex');}
        ,function(){
    $("#desktopDropDownMenu").css('display', 'none');
    });

    $("#id_discount_price").addClass('hide');

});

$("#linkedProductChoice").change(function() {
 console.log("function reached.");
 let val = $(this).val();
 let imagePath = `/static/media/product-images/${val}`;
  $("#linkImageSelection").attr('src', val);
});

