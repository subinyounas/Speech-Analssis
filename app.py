import gradio as gr
from preprocess_audio import preprocess_audio
from transcribe import transcribe_audio
from analyze_sentiment import sentiment_analysis
from summarize_text import summarize_text


# load the audio file
def load_and_process_audio(upload_input, microphone_input):
    if upload_input is not None or microphone_input is not None:
        if upload_input is not None:
            audio_file = upload_input
        else:
            audio_file = microphone_input
        print("Audio File: ", audio_file)

        # Preprocess the audio
        preprocessed_audio, duration = preprocess_audio(audio_file)
        print("Audio Preprocessed")

        # transcribe the audio
        transcribed_text = transcribe_audio(preprocessed_audio)
        print("Audio Transcribed", transcribed_text)
        # sentiment analysis
        sentiment_result = sentiment_analysis(transcribed_text)
        print("Sentiment Analysis Done", sentiment_result)
        sentiment_label = sentiment_result[0]["label"].title()
        sentiment_score = sentiment_result[0]["score"]

        summary = summarize_text(transcribed_text)

        alert_message = "Audio processed successfully!"

        return (
            transcribed_text,
            sentiment_label,
            sentiment_score,
            summary,
            alert_message,
        )
    else:
        alert_message = "Please upload an audio file or record an audio file"
        return "", "", "", "", alert_message


# Create a Gradio interface

# Create the input components
upload_input = gr.Audio(sources="upload", type="filepath", label="Upload an audio file")
microphone_input = gr.Audio(
    sources="microphone", type="filepath", label="Record an audio file"
)

# Create the interface
iface = gr.Interface(
    fn=load_and_process_audio,
    inputs=[upload_input, microphone_input],
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Label(label="Sentiment"),
        gr.Number(label="Sentiment Score"),
        gr.Textbox(label="Summary"),
        gr.Markdown(),
    ],  # Output components
    title="Speech-to-Text & Sentiment Analysis Dashboard",
    description="Analyze the sentiment of an audio file and transcribe the summary",
    theme="gradio/soft",
    allow_flagging="never",
)

# Launch the interface
if __name__ == "__main__":
    iface.launch(share=True)
