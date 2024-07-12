import gensim.downloader as api
from numpy.linalg import norm

glove = api.load("glove-twitter-50")
# glove = api.load("glove-wiki-gigaword-50")

def cosine_sim(word1, word2):
    a = glove[word1]
    b = glove[word2]
    return a.T @ b / (norm(a) * norm(b))

def get_sorted_similarities(clue, wordlist):
        return sorted([(cosine_sim(clue, w), w) for w in wordlist], reverse=True)