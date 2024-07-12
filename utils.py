import gensim.downloader as api
from numpy.linalg import norm

glove = api.load("glove-twitter-50")
# glove = api.load("glove-wiki-gigaword-50")

def cosine_sim(word1, word2):
    '''Calculates the cosine similarity between 2 words based on GloVe embeddings
    Params:
    - word1 (str): first word
    - word2 (str): second word
    Returns:
    - float: cosine similarity fr0m -1 to 1
    '''
    a = glove[word1]
    b = glove[word2]
    return a.T @ b / (norm(a) * norm(b))

def get_sorted_similarities(clue, wordlist):
        '''Sorts words in wordlist in descending order based on cosine similarity to clue
        Params:
        - clue (str): clue word
        - wordlist (list): list of words to check against clue word
        Returns:
        - list: sorted list of (similarity, word), from most similar to least
        '''
        return sorted([(cosine_sim(clue, w), w) for w in wordlist], reverse=True)