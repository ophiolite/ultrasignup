$(document).ready(function() {

    //process the director's form
    $('#directors-form').submit(function(event) {

        console.log("Director's form submitted");

        $.ajax({
            type        : 'POST',
            url         : '/race_director',
            data        : 'formData',
            dataType    : 'html',
            encode      : true,
            success: function(response) { // on success
                //console.log("Results: " + response);
                $('#directors-results').html(response);
            }
        })

        .done(function(data) {
            //console.log(data);
        });

    event.preventDefault();
    });

    // process the model form
    $('#model-form').submit(function(event) {

        console.log("Model form submitted");

        // get the form data
        var formData = JSON.stringify($("#model-form").serializeArray());

        console.log(formData);

        // var formData = {
        //     'age'           : $('input[name=age]').val(),
        //     'gender'        : $('input[name=gender]').val(),
        //     'race'          : $('input[name=race]').val()
        // };

        // process the form
        $.ajax({
            type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
            contentType : "application/json; charset=utf-8",
            url         : '/athlete_proba', // the url where we want to POST
            data        : formData, // our data object
            dataType    : 'html', // what type of data do we expect back from the server
            encode      : true,
            success: function(response) { // on success
                //console.log("Results: " + response);
                $('#model-results').html(response);
                }
        })
            // using the done promise callback
            .done(function(data) {

                // log data to the console so we can see
                //console.log(data);

                // here we will handle errors and validation messages
            });

        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
    });



});
