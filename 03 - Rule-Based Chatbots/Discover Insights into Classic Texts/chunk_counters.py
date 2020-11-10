from collections import Counter


# Function that pulls chunks out of chunked sentence and finds the most common chunks:
def np_chunk_counter(chunked_sentences):
    # List to hold chunks:
    chunks = list()
    # For-loop through each chunked sentence to extract noun phrase chunks:
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))
    # Counter object
    chunk_counter = Counter()
    # For-loop through the list of chunks;
    for chunk in chunks:
        # Increase counter of specific chunk by 1:
        chunk_counter[chunk] += 1
    # Return the 30 most frequent chunks:
    return chunk_counter.most_common(30)


# Function that pulls chunks out of chunked sentence and finds the most common chunks:
def vp_chunk_counter(chunked_sentences):
    # List to hold chunks:
    chunks = list()
    # For-loop through each chunked sentence to extract verb phrase chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))
    # Counter object
    chunk_counter = Counter()
    # For-loop through the list of chunks:
    for chunk in chunks:
        # Increase counter of specific chunk by 1:
        chunk_counter[chunk] += 1
    # Return the 30 most frequent chunks
    return chunk_counter.most_common(30)
