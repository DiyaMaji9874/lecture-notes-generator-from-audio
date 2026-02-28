import streamlit as st
from src.audio_processing import load_whisper_model, transcribe_audio

# --- Page Configuration ---
st.set_page_config(page_title="Lecture Transcription", page_icon="🎙️", layout="wide")

# --- Initialize Models (Cached to save RAM/Time) ---
@st.cache_resource
def get_whisper():
    return load_whisper_model("base")

# --- UI Setup ---
st.title("🎙️ Local Lecture Transcription")
st.write("100% private and local. Whisper transcribes the audio!")

# --- Main Interface ---
audio_file = st.file_uploader("Upload Lecture Audio", type=["mp3", "wav", "m4a", "ogg"])

if st.button("Transcribe Audio"):
    if audio_file is None:
        st.error("Please upload an audio file.")
    else:
        # Transcription
        with st.spinner("🎙️ Transcribing audio using Whisper..."):
            whisper_model = get_whisper()
            transcript = transcribe_audio(audio_file, whisper_model)
        
        st.success("Transcription Complete!")

        # Display Results
        st.subheader("📝 Raw Transcription")
        st.write(transcript)
        
        st.download_button(
            label="Download Transcript as TXT",
            data=transcript,
            file_name="lecture_transcript.txt",
            mime="text/plain"
        )