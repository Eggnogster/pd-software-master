/* ------------------------------------------------------------------------------
*
*  # SelectBoxIt selects
*
*  Specific JS code additions for form_select_box_it.html page
*
*  Version: 1.1
*  Latest update: Feb 5, 2016
*
* ---------------------------------------------------------------------------- */

$(function() {


    // Basic examples
    // ------------------------------

    // Basic initialization
    $(".selectbox").selectBoxIt({
        autoWidth: false
    });


    // Bootstrap theme support
    $('.selectbox-bootstrap').selectBoxIt({
        autoWidth: false,
        theme: "bootstrap"
    });
    
    
    // Allow copying classes to container
    $(".selectbox-container").selectBoxIt({
        autoWidth: false,
        copyClasses: 'container'
    });


    // Custom arrow icon
    $(".selectbox-custom-icon").selectBoxIt({
        autoWidth: false,

        // Set a custom down arrow icon by adding new CSS class(s)
        downArrowIcon: "icon-three-bars"
    });


    // jQuery animations
    $(".selectbox-animated-jquery").selectBoxIt({
        autoWidth: false,

        // Uses the jQuery 'slideDown' effect when opening the drop down
        showEffect: "slideDown",

        // Sets the jQuery 'slideDown' effect speed to 400 milleseconds
        showEffectSpeed: 200,

        // Uses the jQuery 'slideUp' effect when closing the drop down
        hideEffect: "slideUp",

        // Sets the jQuery 'slideUp' effect speed to 400 milleseconds
        hideEffectSpeed: 200
    });


    // Hide first option
    $(".selectbox-hide-first").selectBoxIt({
        autoWidth: false,
        showFirstOption: false // Hides the first select box option from appearing when the drop down is opened
    });


    // Hide current option
    $(".selectbox-hide-current").selectBoxIt({
        autoWidth: false,
        hideCurrent: true // Hides the currently selected option from appearing when the drop down is opened
    });


    // Trigger native select
    $(".selectbox-trigger-native").selectBoxIt({
        autoWidth: false,
        native: true // Triggers the native select box when a user interacts with the drop down
    });


    // Custom default text
    $(".selectbox-default-text").selectBoxIt({
        autoWidth: false,
        defaultText: "Sample text here" // Sets default text to appear for the drop down
    });


    // Aggressive change mode
    $(".selectbox-aggressive").selectBoxIt({
        autoWidth: false,
        aggressiveChange: true // Sets default text to appear for the drop down
    });


    // Native mousedown mode
    $(".selectbox-mousedown").selectBoxIt({
        autoWidth: false,
        nativeMousedown: true // Sets default text to appear for the drop down
    });




    // Array of objects
    $(".selectbox-objects-array").selectBoxIt({
        autoWidth: false,

        // Populates the drop down using an array of objects
        populate: [
            {value: "SelectBoxIt is:", text: "SelectBoxIt is:"},
            {value: "a jQuery Plugin", text: "a jQuery Plugin"},
            {value: "a Select Box Replacement", text: "a Select Box Replacement"},
            {value: "a Stateful UI Widget", text: "a Stateful UI Widget"}
        ]
    });


    // Single object
    $(".selectbox-single-object").selectBoxIt({
        autoWidth: false,

        // Populates the drop down using an array of strings
        populate: {
            value: "SelectBoxIt is:",
            text: "SelectBoxIt is:"
        }
    });


    // HTML string
    $(".selectbox-html-string").selectBoxIt({
        autoWidth: false,

        // Populates the drop down using a JSON array
        populate: '<option value="SelectBoxIt is:">SelectBoxIt is:</option>' +
            '<option value="a jQuery Plugin">a jQuery Plugin</option>' +
            '<option value="a Select Box Replacement">a Select Box Replacement</option>' +
            '<option value="a Stateful UI Widget">a Stateful UI Widget</option>'
    });



    // Option manipulations
    // ------------------------------

    //
    // Dynamic options
    //


    //
    // Remove first option dynamically
    //

    // Other additions
    // ------------------------------

    // Enable popover
    $('[data-toggle="popover"').popover();
    
});
