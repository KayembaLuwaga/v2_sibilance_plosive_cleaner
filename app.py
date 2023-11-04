# app.py
from flask import Flask, request, render_template, send_from_directory
from audio_processing.audio_processing import process_audio
import os

app = Flask(__name__)

# Define the folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_audio = None  # Initialize processed_audio as None
    cutoff_frequency = 1000  # Default cutoff frequency
    silence_thresh = -40  # Default silence threshold

    if request.method == 'POST':
        if 'audio' in request.files:
            audio_file = request.files['audio']
            if audio_file.filename != '':
                audio_file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_audio.wav'))

        remove_sibilance = 'remove_sibilance' in request.form
        remove_plosive = 'remove_plosive' in request.form
        clean = 'clean' in request.form

        # Get user-input cutoff_frequency and silence_thresh values
        cutoff_frequency = int(request.form.get('cutoff_frequency', 1000))
        silence_thresh = int(request.form.get('silence_thresh', -40))

        # Process audio only if the uploaded file exists
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_audio.wav')):
            processed_audio = process_audio(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_audio.wav'), remove_sibilance, remove_plosive, cutoff_frequency, silence_thresh)
            processed_audio.export('static/uploads/processed_audio.wav', format='wav')

    return render_template('index.html', processed_audio=processed_audio)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('static/uploads', filename)

@app.route('/download_processed_audio')
def download_processed_audio():
    return send_from_directory('static/uploads', 'processed_audio.wav', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
