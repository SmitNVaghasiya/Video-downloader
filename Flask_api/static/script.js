$(document).ready(function () {
    // Handle form submission
    $('#downloadForm').on('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        var url = $('#urlInput').val(); // Get the URL from the input field

        $.ajax({
            type: 'POST',
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

                    // Update the title and thumbnail in the HTML
                    $('.description-card.description').text(response.title);
                    $('.picture-card img').attr('src', response.thumbnail);

                    // Show the below container
                    $('.below-container').removeClass('hidden');
                }
            },
            error: function () {
                // Handle any errors that occur during the AJAX request
                $('#responseContainer').html('An error occurred.');
            }
        });
    });

    // Regular expression to match YouTube URLs
    const youtubeUrlPattern = /^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)(?:\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$/;

    // Event listener for input field
    $('#urlInput').on('input', function () {
        const urlInput = $(this).val().trim();
        const belowContainer = $('.below-container');

        if (urlInput !== "" && youtubeUrlPattern.test(urlInput)) {
            belowContainer.removeClass('hidden');
        } else {
            belowContainer.addClass('hidden');
        }
    });
});
