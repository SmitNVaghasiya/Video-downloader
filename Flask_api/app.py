from flask import Flask, request, jsonify, send_file, render_template
from video_downloader import download_video 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')
    # return render_template('index.html')


@app.route('/download', methods=['GET'])
def download():
    url = request.form.get('url')
    print(url)
    directory = '/path/to/temp'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Download video
    filename, error = download_video(url, directory)
    
    if error:
        return jsonify({'error': error}), 400

    # Return the filename for download URL construction
    return jsonify({'filename': filename})

@app.route('/download_file/<filename>')
def download_file(filename):
    directory = '/path/to/temp'
    return send_file(
        os.path.join(directory, filename),
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True)
