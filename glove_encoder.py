from itertools import combinations
import numpy as np

class GloVeEncoder():
    def __init__(self, decoder, glove, power = 5, n_candidates = 10):
        self.power = power
        self.decoder = decoder
        self.glove = glove
        self.n_candidates = n_candidates
    
    def score_clue(self, clue, number, mywords, wordlist, danger): 
        preds = self.decoder.decode(clue, number, wordlist)
        if danger in preds:
            return -1e9
        cnt = 0
        for word in preds:
            if word in mywords:
                cnt += 1
            else:
                break
        return cnt
    
    def get_closest_words(self, good_words, wordlist):

        return [word for word, _ in self.glove.most_similar(np.mean([self.glove[word] for word in good_words], axis=0)) if word not in wordlist][:self.n_candidates]

    def encode(self, mywords, wordlist, danger):
        maxscore = -1e9
        clue = ""
        number = 0
        for n in range(1, self.power + 1):
            for good_words in combinations(mywords, n):
                candidates = self.get_closest_words(good_words, wordlist)
                for candidate in candidates:
                    score = self.score_clue(candidate, n, mywords, wordlist, danger)
                    if score > maxscore:
                        maxscore = score
                        clue = candidate
                        number = n
        return clue, number