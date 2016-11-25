$(document).ready(function() {

    //process the director's form
    $('#directors-form').submit(function(event) {

        console.log("Director's form submitted");

        $.ajax({
            type        : 'POST',
            url         : 'https://app-name.heroku.com/endpoint',
            data        : 'formData',
            dataType    : 'json',
            encode      : true
        })

        .done(function(data) {
            console.log(data);
        });

    event.preventDefault();
    });

    // process the model form
    $('#model-form').submit(function(event) {

        // get the form data
        // there are many ways to get this data using jQuery (you can use the class or id also)
        var formData = {
            'age'           : $('input[name=age]').val(),
            'gender'        : $('input[name=gender]').val(),
            'race'          : $('input[name=race]').val()
        };

        // process the form
        $.ajax({
            type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
            url         : 'https://app-name.heroku.com/endpoint', // the url where we want to POST
            data        : formData, // our data object
            dataType    : 'json', // what type of data do we expect back from the server
                        encode          : true
        })
            // using the done promise callback
            .done(function(data) {

                // log data to the console so we can see
                console.log(data);

                // here we will handle errors and validation messages
            });

        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
    });



});
