import librosa


def preprocess_audio(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=16000)

    duration = librosa.get_duration(y=y, sr=sr)
    print(f"Audio duration: {duration} seconds")
    # Trim the audio
    y_trimmed, _ = librosa.effects.trim(y)
    # Normalize the audio
    y_normalized = librosa.util.normalize(y_trimmed)
    # Denoise the audio
    y_denoised = librosa.effects.preemphasis(y_normalized)

    return y_denoised, duration
