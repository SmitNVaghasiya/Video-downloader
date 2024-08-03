from flask import Flask, request, jsonify, send_file, render_template
from video_downloader import download_video 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')
    return render_template('index.html')


@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')  # Use request.args for GET parameters
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    directory = 'temp'  # You can use a relative path or configure as needed

    filename, error = download_video(url, directory)
    
    if error:
        return jsonify({'error': error}), 400

    return jsonify({'filename': filename})

@app.route('/download_file/<filename>')
def download_file(filename):
    directory = 'temp'
    filepath = os.path.join(directory, filename)
    
    if not os.path.isfile(filepath):
        return jsonify({'error': 'File not found'}), 404

    return send_file(
        filepath,
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True)
