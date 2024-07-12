from itertools import combinations
import numpy as np

class GloVeEncoder():
    def __init__(self, decoder, glove, number_range = 3):
        self.number_range = number_range
        self.decoder = decoder
        self.glove = glove
    
    def score_clue(self, clue, number, mywords, wordlist, danger): 
        preds = self.decoder.decode(clue, number, wordlist)
        if danger in preds:
            return 0
        cnt = 0
        for word in preds:
            if word in mywords:
                cnt += 1
            else:
                break
        return cnt
    
    def get_closest_word(self, good_words, wordlist):
        for word, _ in self.glove.most_similar(np.mean([self.glove[word] for word in good_words], axis=0)):
            if word not in wordlist:
                return word

    def encode(self, mywords, wordlist, danger):
        maxscore = -1e9
        clue = ""
        number = 0
        for n in range(1, self.number_range + 1):
            for good_words in combinations(mywords, n):
                candidate = self.get_closest_word(good_words, wordlist)
                score = self.score_clue(candidate, n, mywords, wordlist, danger)
                if score > maxscore:
                    maxscore = score
                    clue = candidate
                    number = n
        return clue, number