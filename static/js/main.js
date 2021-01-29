// Counting the basket items - outside document ready for functionality
$('#addToBasket').click(function(){
    item = sessionStorage.getItem('currentBasketAmount')
    if (item == null){
        sessionStorage.setItem('currentBasketAmount', 0);
        sessionStorage.setItem('newBasketAmount', 1);
    } else{
        item++;
        sessionStorage.setItem('newBasketAmount', item)
    }
});

// Emptying basket - outside document ready for functionality
$('#emptyBasket').click(function(){
    sessionStorage.clear();
});


$( document ).ready(function() {
    // Revealing desktop nav - Taken from jQuery documentation
    $("#desktopExtraNavWrapper").hover(function(){
            $("#desktopDropDownMenu").css('display', 'flex');
        } , function(){
            $("#desktopDropDownMenu").css('display', 'none');
            }
        );
    
    // Profiles 
    // Revealing previous purchases
    $('#previousPurchaseHeader, #revealPreviousPurchase').click(function(){
        $('#previousPurchaseWrapper, #previousPurchaseHr').toggleClass('hide');    
    });

    $("#adminProductManage").change(function() {
        $('.allProducts').addClass('hide');
        let val = $(this).val();
        $(`.adminCategory${val}`).toggleClass(' hide');
        $(`#adminCategoryHR`).removeClass(' hide'); 
    });
    
    // Basket
    // Triggering the 'added item' animation
    let currentBasketAmount = sessionStorage.getItem('currentBasketAmount')
    let newBasketAmount = sessionStorage.getItem('newBasketAmount')

    if(newBasketAmount > currentBasketAmount){
        $(".fa-shopping-basket").addClass('item-added-transition');
        sessionStorage.setItem('currentBasketAmount', newBasketAmount)
    } else{
           $(".fa-shopping-basket").removeClass('item-added-transition');
    }


    // Altering product quantity from Product Detail
    $('#increaseProductDetailQuantity').click(function(e){
        e.preventDefault();
        let quantity = parseInt($('#productDetailQty').val());
            $('#productDetailQty').val(quantity + 1);   
            $('#addToBasket').prop('disabled', false);
    });

    $('#decreaseProductDetailQuantity').click(function(e){
        e.preventDefault();
        let quantity = parseInt($('#productDetailQty').val());
        if (quantity > 1){         
            $('#productDetailQty').val(quantity - 1);
        } else {
            quantity = 0;
            $('#productDetailQty').val(quantity);
            $('#addToBasket').prop('disabled', true);
        }
    });

    // Disabling the quantity button on Product Detail depending on the delivery method.
    let digital_counter = 0
    $("#deliveryTypeCheckbox").change(function() {
        digital_counter++;
        
        if (digital_counter % 2 == 0){
            $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', false);
            var quantity = 1;
            $('#productDetailQty').val(quantity);
        } else {
            $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', true);
        var quantity = 1;
            $('#productDetailQty').val(quantity);
        }
    
    });

    // Enabling the 'quantity' field as a reset from the function above. 
    $('#addToBasket').click(function(){
        $("#productDetailQty").prop('disabled', false);
    
    });


    // Review reveal
    $('#reviewTrigger').click(function(){
        $("#reviewsWrapper").toggleClass('hide');
    });


    // Linked products preview image - live changes
    $(".linkingProductSelect").change(function() {

    // Getting the image path from the select
    let val = $(this).val();
    let splittingValues = val.split("|");
    let imageType = splittingValues[2];

    // Different options are then chosen based on image type.
    if (imageType == "inventory") {
        let imagePath = splittingValues[0];
        $("#linkImageSelection").attr('src', imagePath);
        $("#linkedProductImagePreview").attr('href', imagePath);
        $("#linkImageHint, #linkImageSelection, #linkedProductImagePreview").removeClass('hide');
        $("#linkImageSelection").addClass('product-linked-preview');

    } else if(imageType == "No item"){
        imagePath = "/static/media/site_images/white_square.jpg"
        $("#linkImageSelection").attr('src', imagePath);
        $("#linkImageSelection, #linkedProductImagePreview, #linkImageHint").addClass('hide');

    } else {
        let imagePath = "/media/" + splittingValues[0];
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

    // Altering the quantity of a basket item
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

    //  Edit review quantity and capping the score at 5 or 0
    $('#increaseEditReviewQuantity').click(function(e){
        e.preventDefault();
        let quantity = parseInt($('#edit_review_rating').val()); 
        if (quantity == 5){  
            quantity = 5;      
            $('#edit_review_rating').val(quantity);
        } else {   
            $('#edit_review_rating').val(quantity + 1);
        }          
    });

    $('#decreaseEditReviewQuantity').click(function(e){
        e.preventDefault();
        let quantity = parseInt($('#edit_review_rating').val());
        if (quantity > 1){         
            $('#edit_review_rating').val(quantity - 1);
        } else {
            quantity = 0;
            $('#edit_review_rating').val(quantity);
        }
    });

    // Add review and capping the score at 5 or 0
    $('#increaseAddReviewQuantity').click(function(e){
        e.preventDefault();
        let quantity = parseInt($('#add_review_rating').val());
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
        if (quantity > 1){         
            $('#add_review_rating').val(quantity - 1);
        } else {
            quantity = 0;
            $('#add_review_rating').val(quantity);
        }
    });
});