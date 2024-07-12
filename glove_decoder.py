from utils import get_sorted_similarities

class GloVeDecoder():
    def decode(self, clue, number, wordlist):
        '''Decodes a clue and number
        Params:
        - clue (str): clue given by encoder
        - number (int): number n given by encoder
        - wordlist (list): current words still in play
        Returns:
        - list: n most probable words, sorted from highest probability, of words in wordlist
        '''
        return [w for _, w in get_sorted_similarities(clue, wordlist)[:number]]