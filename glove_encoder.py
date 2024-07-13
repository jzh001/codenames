from itertools import combinations
import random
from math import comb
import re

class GloVeEncoder():
    def __init__(self, decoder, glove, n_candidates, n_negative_samples):
        self.decoder = decoder
        self.glove = glove
        self.n_candidates = n_candidates
        self.n_negative_samples = n_negative_samples
    
    def score_clue(self, clue, number, mywords, wordlist): 
        '''Scores a clue and number based on number of words decoder gets correct. Stops before getting a wrong or danger word.
        Params:
        - clue: candidate clue to test
        - number: chosen number to test
        - mywords: good words remaining
        - wordlist: all words remaining
        Returns:
        - int: number of words gotten correct by decoder
        '''
        preds = self.decoder.decode(clue, number, wordlist)
        cnt = 0
        for word in preds:
            if word in mywords:
                cnt += 1
            else:
                break
        return cnt

    def isalpha(self, s):
        return bool(re.match(r'^[a-z]+$', s))
    
    def get_closest_words(self, good_words, bad_words, wordlist):
        '''Given a set of good and bad words, find candidate clues which maximizes cosine similarity with good words and maximizes cosine distance with bad words
        Params:
        - good_words (tuple): tuple of good words
        - bad_words (list): list of bad words
        - wordlist (set): set of all words
        Returns:
        - set: candidate clues
        '''
        negatives = [random.sample(bad_words, min(len(bad_words), len(good_words))) for _ in range(min(self.n_negative_samples, comb(len(bad_words), min(len(bad_words), len(good_words)))))]
        return set([word for negative in negatives for word, _ in self.glove.most_similar(positive=list(good_words), negative=negative, topn=self.n_candidates) if word not in wordlist and self.isalpha(word)])

    def encode(self, mywords, wordlist):
        '''Given a set of words, encode into {clue, number}
        Params:
        - mywords (list): list of remaining good words
        - wordlist (list): list of all remaining words
        Returns:
        - tuple(str, int): chosen clue and number
        '''
        maxscore = -1e9
        clue = ""
        number = 0
        bad_words = [word for word in wordlist if word not in mywords]
        for n in range(len(mywords), 0, -1):
            if maxscore >= n:
                break
            for good_words in combinations(mywords, n):
                candidates = self.get_closest_words(good_words, bad_words, wordlist)
                for candidate in candidates:
                    score = self.score_clue(candidate, n, mywords, wordlist)
                    if score > maxscore:
                        maxscore = score
                        clue = candidate
                        number = score
        return clue, number