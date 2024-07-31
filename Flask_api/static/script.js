$(document).ready(function () {
    $('#downloadForm').on('submit', function (event) {
        event.preventDefault();

        var url = $('#urlInput').val();
        console.log(url);

        $.ajax({
            type: 'POST',
            url: '/download',
            data: { url: url },
            dataType: 'json',
            success: function (response) {
                $('#responseContainer').html('Download started: ' + response.message);
            },
            error: function () {
                $('#responseContainer').html('An error occurred.');
            }
        });
    });
});
