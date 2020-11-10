from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter


def natural_language_parser(text):
    text = open(f"{text}.txt", encoding='utf-8').read().lower()
    # Split the text into individual sentences and then individual words:
    word_tokenized_text = word_sentence_tokenize(text)
    # Print any tokenized word sentence:
    print(word_tokenized_text[100])
    # Create a list to hold part-of-speech tagged sentences:
    pos_tagged_text = [pos_tag(word) for word in word_tokenized_text]
    # Print any part-of-speech tagged sentence:
    print(pos_tagged_text[100])
    # Define noun phrase chunk grammar:
    np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
    # Create noun phrase RegexpParser object:
    np_chunk_parser = RegexpParser(np_chunk_grammar)
    # Define verb phrase chunk grammar::
    vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"
    # Create verb phrase RegexpParser object:
    vp_chunk_parser = RegexpParser(vp_chunk_grammar)
    # List of noun phrase chunked sentences:
    np_chunked_text = []
    # List of verb phrase chunked sentences:
    vp_chunked_text = []
    for sentence in pos_tagged_text:
        np_chunked_text.append(np_chunk_parser.parse(sentence))
        # List of verb phrase chunked sentences:
        vp_chunked_text.append(vp_chunk_parser.parse(sentence))
    # Most commons chunks:
    most_common_np_chunks = np_chunk_counter(np_chunked_text)
    most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
    print(most_common_np_chunks)
    print(most_common_vp_chunks)


if __name__ == '__main__':
    natural_language_parser("dorian_gray")
