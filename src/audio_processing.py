import whisper
import tempfile
import os

def load_whisper_model(model_name="base"):
    """Loads and caches the Whisper model."""
    return whisper.load_model(model_name)

def transcribe_audio(uploaded_file, model):
    """Saves the uploaded file temporarily and transcribes it."""
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_filename = tmp_file.name

    try:
        # Transcribe the audio
        result = model.transcribe(tmp_filename)
        return result["text"]
    finally:
        # Ensure the temporary file is deleted even if an error occurs
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
