from transformers import pipeline


# sentiment analyis
def sentiment_analysis(text):
    sentiment_analyzer = pipeline(
        "sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion"
    )
    sentiment = sentiment_analyzer(text)
    return sentiment
