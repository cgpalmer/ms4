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

$(".linkingProductSelect").change(function() {
 console.log("function reached.");
 let val = $(this).val();
 let splittingValues = val.split("|");
 let imageType = splittingValues[2];
 let imageId = splittingValues[1]
 if (imageType == "inventory") {
    let imagePath = splittingValues[0];
    console.log(imagePath);
  $("#linkImageSelection").attr('src', imagePath);
  $("#linkedProductImagePreview").attr('href', imagePath);
 } else {
     let imagePath = "/media/" + splittingValues[0];
     console.log(imagePath);
  $("#linkImageSelection,  ").attr('src', imagePath);
  $("#linkedProductImagePreview").attr('href', imagePath);

 }
 
});



function updateBasket(editId, updateId, cancelId, editQuantity, editDelivery, editLinkedItem, editMode) {
    let editButton = document.getElementById(editId);
    let updateButton = document.getElementById(updateId);
    let cancelButton = document.getElementById(cancelId);
    let quantityEdit = document.getElementById(editQuantity);
    let deliveryEdit = document.getElementById(editDelivery);
    let editItem = document.getElementById(editLinkedItem);
    console.log(editItem)
    let editingMode = editMode;
    if (editingMode == 'update'){
        editButton.classList.add('hide')
        updateButton.classList.remove('hide')
        cancelButton.classList.remove('hide')
        quantityEdit.classList.remove('hide')
        deliveryEdit.classList.remove('hide')
        editItem.classList.remove('hide')
    } else {
        editButton.classList.remove('hide')
        updateButton.classList.add('hide')
        cancelButton.classList.add('hide')
        quantityEdit.classList.add('hide')
        deliveryEdit.classList.add('hide')
        editItem.classList.add('hide')
    }
    
}



