 $('#addToBasket').click(function(){
        item = sessionStorage.getItem('currentBasketAmount')
        if (item == null){
            sessionStorage.setItem('currentBasketAmount', 0);
             sessionStorage.setItem('newBasketAmount', 1);
        } else{
            item++;
            sessionStorage.setItem('newBasketAmount', item)
        }
        console.log(item);
 });

$('#emptyBasket').click(function(){
    sessionStorage.clear();
    console.log("should clear");
});


$( document ).ready(function() {
    console.log( " defs ready!" );
 
     $("#desktopExtraNavWrapper").hover(function(){
        $("#desktopDropDownMenu").css('display', 'flex');}
        ,function(){
    $("#desktopDropDownMenu").css('display', 'none');
});
    $('#previousPurchaseHeader, #revealPreviousPurchase').click(function(){
        console.log("reached");
      $('#previousPurchaseWrapper, #previousPurchaseHr').toggleClass('hide');

         
    });


    
    let currentBasketAmount = sessionStorage.getItem('currentBasketAmount')
    let newBasketAmount = sessionStorage.getItem('newBasketAmount')
    console.log(currentBasketAmount)
    console.log(newBasketAmount)
    if(newBasketAmount > currentBasketAmount){
        $(".fa-shopping-basket").addClass('item-added-transition');
        sessionStorage.setItem('currentBasketAmount', newBasketAmount)
        // $(".fa-shopping-basket").removeClass('item-added-transition');
    } else{
           $(".fa-shopping-basket").removeClass('item-added-transition');
    }

});


// Nav bar



// Hiding the photo upload function

$('#imageUploadWrapperTrigger').click(function(){
    $('#imageUploadWrapper').toggleClass('hide');
});

// Increasing product quantity

$('#increaseProductDetailQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#productDetailQty').val());
        
        // If is not undefined
            
            $('#productDetailQty').val(quantity + 1);
       
            $('#addToBasket').prop('disabled', false);
        
});

$('#decreaseProductDetailQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#productDetailQty').val());
        
        // If is not undefined
    if (quantity > 1){         
        $('#productDetailQty').val(quantity - 1);
    } else {
        quantity = 0;
         $('#productDetailQty').val(quantity);

        $('#addToBasket').prop('disabled', true);
    }
});

let digital_counter = 0
$("#deliveryTypeCheckbox").change(function() {
    digital_counter++;
    
    if (digital_counter % 2 == 0){
        console.log(digital_counter);
         $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', false);
        var quantity = 1;
         $('#productDetailQty').val(quantity);
    } else {
        console.log("odd");
        $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', true);
      var quantity = 1;
        $('#productDetailQty').val(quantity);
    }
   
});

$('#addToBasket').click(function(){
    $("#productDetailQty").prop('disabled', false);
   
});


// Review reveal

$('#reviewTrigger').click(function(){
    console.log("triggered");
    $("#reviewsWrapper").toggleClass('hide');
});

// Linked products
$(".linkingProductSelect").change(function() {
 console.log("function reached.");
 let val = $(this).val();
 console.log(val)
 let splittingValues = val.split("|");
 let imageType = splittingValues[2];
 if (imageType == "inventory") {
    let imagePath = splittingValues[0];
    console.log(imagePath);
  $("#linkImageSelection").attr('src', imagePath);
  $("#linkedProductImagePreview").attr('href', imagePath);
   $("#linkImageHint, #linkImageSelection, #linkedProductImagePreview").removeClass('hide');
  
  $("#linkImageSelection").addClass('product-linked-preview');
 } else if(imageType == "No item"){
    imagePath = "/static/media/product-images/white_square.jpg"
    $("#linkImageSelection").attr('src', imagePath);
    $("#linkImageSelection, #linkedProductImagePreview, #linkImageHint").addClass('hide');
 } else {
     let imagePath = "/media/" + splittingValues[0];
     console.log(imagePath);
  $("#linkImageSelection").attr('src', imagePath);
  $("#linkImageSelection").addClass('product-linked-preview');
  $("#linkedProductImagePreview").attr('href', imagePath);
  $("#linkImageHint, #linkImageSelection, #linkedProductImagePreview").removeClass('hide');

 }
 
});

// Update basket





$('.quantityModifier').click(function(e){
    e.preventDefault();
});


$("#adminProductManage").change(function() {
    console.log("triggered")
    $('.allProducts').addClass('hide');
    let val = $(this).val();
    console.log(val);
    $(`.adminCategory${val}`).toggleClass(' hide');
    $(`#adminCategoryHR`).removeClass(' hide');
  
    
});






function decreaseBasketQuantity(element){
    
    let splittingElementID = element.split("_");
    let quantityInputID = `#productDetailQty_${splittingElementID[1]}`;
    let quantity = parseInt($(quantityInputID).val());
    if (quantity > 1){         
        $(quantityInputID).val(quantity - 1);
    } else {
        quantity = 0;
         $(quantityInputID).val(quantity);
    }
};

function increaseBasketQuantity(element){

    let splittingElementID = element.split("_");
    let quantityInputID = `#productDetailQty_${splittingElementID[1]}`;
    let quantity = parseInt($(quantityInputID).val()); 
    $(quantityInputID).val(quantity + 1);
   
};



//  Edit review quantity

$('#increaseEditReviewQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#edit_review_rating').val());
    
    if (quantity == 5){  
        quantity = 5;      
        $('#edit_review_rating').val(quantity);
    } else {   
            $('#edit_review_rating').val(quantity + 1);
    }          
        
});

$('#decreaseEditReviewQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#edit_review_rating').val());
        
        // If is not undefined
    if (quantity > 1){         
        $('#edit_review_rating').val(quantity - 1);
    } else {
        quantity = 0;
         $('#edit_review_rating').val(quantity);
    }
});

// Add review
$('#increaseAddReviewQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#add_review_rating').val());
    
    if (quantity == 5){  
        quantity = 5;      
        $('#add_review_rating').val(quantity);
    } else {   
            $('#add_review_rating').val(quantity + 1);
    }          
        
});

$('#decreaseAddReviewQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#add_review_rating').val());
        
        // If is not undefined
    if (quantity > 1){         
        $('#add_review_rating').val(quantity - 1);
    } else {
        quantity = 0;
         $('#add_review_rating').val(quantity);
    }
});