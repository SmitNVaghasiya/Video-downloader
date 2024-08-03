$(document).ready(function () {
    // Event handler for form submission
    $('#downloadForm').on('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        var url = $('#urlInput').val(); // Get the URL from the input field
        console.log(url); // Log the URL for debugging

        $.ajax({
            type: 'GET', // Changed to GET to match the Flask route
            url: '/download',
            data: { url: url },
            dataType: 'json',
            success: function (response) {
                // Check if there's an error in the response
                if (response.error) {
                    $('#responseContainer').html('Error: ' + response.error);
                } else {
                    // Provide a download link if the video is successfully downloaded
                    $('#responseContainer').html('Download started: <a href="/download_file/' + encodeURIComponent(response.filename) + '">Click here to download</a>');
                }
            },
            error: function () {
                // Handle any errors that occur during the AJAX request
                $('#responseContainer').html('An error occurred.');
            }
        });
    });
});