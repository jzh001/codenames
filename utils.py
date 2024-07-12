from numpy.linalg import norm

def cosine_sim(word1, word2, glove):
    '''Calculates the cosine similarity between 2 words based on GloVe embeddings
    Params:
    - word1 (str): first word
    - word2 (str): second word
    Returns:
    - float: cosine similarity from -1 to 1
    '''
    a = glove[word1]
    b = glove[word2]
    return a.T @ b / (norm(a) * norm(b))

def get_sorted_similarities(clue, wordlist, glove):
    '''Sorts words in wordlist in descending order based on cosine similarity to clue
    Params:
    - clue (str): clue word
    - wordlist (list): list of words to check against clue word
    Returns:
    - list: sorted list of (similarity, word), from most similar to least
    '''
    return sorted([(cosine_sim(clue, w, glove), w) for w in wordlist], reverse=True)