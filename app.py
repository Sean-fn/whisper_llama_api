from flask import Flask, request, jsonify, abort
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = '/Users/sean/Downloads/download'
ALLOWED_EXTENSIONS = {'wav'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if not allowed_file(file.filename):
        return jsonify(error="File type not allowed"), 400
    if file and allowed_file(file.filename):
        file_id = str(uuid.uuid4())
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id + '.wav')
        file.save(file_path)
        return jsonify(file_id=file_id), 200

@app.route('/api/process/<file_id>', methods=['GET'])
def process_file(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id + '.wav')
    if not os.path.exists(file_path):
        abort(404)
    
    # 使用 Whisper 進行語音識別
    text = process_audio_with_whisper(file_path)

    # 使用 llama 進行處理
    gpt_response = process_text_with_llama(text)

    return jsonify(whisper_text=text, gpt_response=gpt_response)


def process_audio_with_whisper(file_path):

    os.remove(file_path)
    return True

def process_text_with_llama(text):
    pass

if __name__ == '__main__':
    app.run(debug=True)
