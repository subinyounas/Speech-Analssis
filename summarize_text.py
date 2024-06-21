from preprocess_text import preprocess_text
import ollama


# summarize text
def summarize_text(text):
    preprocessed_text = preprocess_text(text)
    prompt = f"// Summarize the following preproccessed text from an audio transcription: {preprocessed_text}.//"
    result = ollama.generate(prompt=prompt, model="mistral")
    summary = result["response"]
    return summary
