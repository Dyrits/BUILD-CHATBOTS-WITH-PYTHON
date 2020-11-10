from nltk.tokenize import PunktSentenceTokenizer, word_tokenize


def word_sentence_tokenize(text):
    # PunktSentenceTokenizer:
    sentence_tokenizer = PunktSentenceTokenizer(text)
    # Tokenize text:
    sentence_tokenized = sentence_tokenizer.tokenize(text)
    # Tokenize words (and return as a list):
    return [word_tokenize(word) for word in sentence_tokenized]
