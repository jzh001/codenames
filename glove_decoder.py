from utils import get_sorted_similarities

class GloVeDecoder():
    def decode(self, clue, number, wordlist):
        return [w for _, w in get_sorted_similarities(clue, wordlist)[:number]]