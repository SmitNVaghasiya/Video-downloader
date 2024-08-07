$(document).ready(function () {
    $('#urlInput').on('input', function () {
        var url = $(this).val();
        if (url) {
            $('#loadingCircle').show();  // Show the loading circle
            $.ajax({
                type: 'POST',
                url: '/fetch_details',
                data: { url: url },
                dataType: 'json',
                success: function (response) {
                    $('#loadingCircle').hide();  // Hide the loading circle
                    if (response.error) {
                        $('#videoDescription').text('Error: ' + response.error);
                        $('#videoThumbnail').attr('src', '');
                        $('.below-container').addClass('hidden');
                    } else {
                        $('#videoDescription').text(response.title);
                        $('#videoThumbnail').attr('src', response.thumbnail);
                        var formatsHtml = '';
                        response.formats.forEach(function (format) {
                            formatsHtml += `
                                <div class="option">
                                    <span>${format.format_note}, ${format.resolution}, ${format.filesize}</span>
                                    <button class="downloadButton" data-format-id="${format.format_id}">Download</button>
                                </div>
                            `;
                        });
                        $('.download-card.options').html(formatsHtml);
                        $('.below-container').removeClass('hidden');
                    }
                },
                error: function () {
                    $('#loadingCircle').hide();  // Hide the loading circle
                    $('#videoDescription').text('An error occurred.');
                    $('#videoThumbnail').attr('src', '');
                    $('.below-container').addClass('hidden');
                }
            });
        }
    });

    $(document).on('click', '.downloadButton', function () {
        var url = $('#urlInput').val();
        var formatId = $(this).data('format-id');
        $.ajax({
            type: 'POST',
            url: '/download',
            data: { url: url, format_id: formatId },
            dataType: 'json',
            success: function (response) {
                if (response.error) {
                    $('#responseContainer').html('Error: ' + response.error);
                } else {
                    $('#responseContainer').html('Download started: <a href="/download_file/' + encodeURIComponent(response.filename) + '">Click here to download</a>');
                }
            },
            error: function () {
                $('#responseContainer').html('An error occurred.');
            }
        });
    });
});
