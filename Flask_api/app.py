from flask import Flask, request, jsonify, send_file, render_template
import os
from details_featcher import fetch_video_info
from video_downloader import download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/fetch_details', methods=['POST'])
def fetch_details():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    info, available_formats = fetch_video_info(url)
    if info is None:
        return jsonify({'error': 'Failed to fetch video info'}), 400

    title = info.get('title', 'No title available')
    thumbnail = info.get('thumbnail', '')
    return jsonify({'title': title, 'thumbnail': thumbnail, 'formats': available_formats})

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    format_id = request.form.get('format_id')
    if not url or not format_id:
        return jsonify({'error': 'URL and format_id parameters are required'}), 400

    directory = 'temp'
    filename, error, title, thumbnail = download_video(url, format_id, directory)
    
    if error:
        return jsonify({'error': error}), 400

    return jsonify({'filename': filename, 'title': title, 'thumbnail': thumbnail})

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
    app.run(host='0.0.0.0', port=5000,debug=True)
