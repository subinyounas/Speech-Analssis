import spacy

nlp = spacy.load("en_core_web_sm")
filler_words = {"um", "uh", "like", "you know", "i mean", "so"}


def preprocess_text(text):
    # Tokenize the text
    doc = nlp(text)
    preprocessed_sentences = []

    for sent in doc.sents:
        preprocessed_tokens = []

        for token in sent:
            if (
                token.text.lower() not in filler_words
                and not token.is_stop
                and not token.is_punct
            ):
                preprocessed_tokens.append(token.lemma_.lower())
        preprocessed_sentence = " ".join(preprocessed_tokens)
        preprocessed_sentences.append(preprocessed_sentence)

    preprocessed_text = " ".join(preprocessed_sentences)
    return preprocessed_text
