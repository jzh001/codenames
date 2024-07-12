import random

class Game():
    def __init__(self, encoder, decoder, glove = None, n_words=25, n_good_words = 12, dictionary_path = './wordlist-eng.txt', verbose = 1):
        # https://github.com/Gullesnuffs/Codenames/blob/master/wordlist-eng.txt
        self.dictionary = [word for word in open(dictionary_path, 'r').read().lower().split('\n') if glove == None or word in glove.key_to_index]
        self.decoder = decoder
        self.encoder = encoder
        wordlist = random.sample(self.dictionary, n_words)
        assert(n_good_words + 1 <= n_words)
        tmp = random.sample(wordlist, n_good_words + 1)
        self.mywords = set(tmp[:-1])
        self.num_mywords = len(self.mywords)
        self.danger = tmp[-1]
        self.wordlist = set(wordlist)
        self.turns = 0
        self.correct = 0
        self.guesses = []
        self.verbose = verbose
        if self.verbose > 0:
            print("Codenames Dictionary Size:",len(self.dictionary))
            print("Words", self.wordlist)
            print("My Words", self.mywords)
            print("Danger", self.danger)

    
    def startGame(self):

        history = {
            'wordlist': list(self.wordlist),
            'mywords': list(self.mywords),
            'danger': self.danger,
            'history': []
        }

        while not self.isGameOver():
            self.turns += 1
           
            clue, number = self.encoder.encode(self.mywords, self.wordlist, self.danger)
            if self.verbose > 0:
                print(f"------ Turn {self.turns} ------")
                print("Clue:", clue, number)

            history['history'].append({'clue': clue,
                            'number': number, 
                            'guesses': [],
                            'correct': [],
                            })
            for g in self.decoder.decode(clue, number, self.wordlist):
                history['history'][-1]['guesses'].append(g)
                if not self.guess(g):
                    break
                else:
                    history['history'][-1]['correct'].append(g)
        if self.verbose > 0:
            print("------ Game Over ------")
            print("Statistics: ")
            print(f"My Words: {self.num_mywords} | Turns = {self.turns} | Correct Words Per Turn {self.correct / self.turns:.2f} | % Correct = {self.correct / len(self.guesses) * 100:.2f}%")
            if self.danger in self.guesses:
                print("Danger Word Chosen!")
        return history
            

    def guess(self, word):
        print("Guess:", word)
        self.guesses.append(word)
        self.wordlist.remove(word)
        if word in self.mywords:
            self.correct += 1
            self.mywords.remove(word)
            print("Correct!")
            return True
        elif word == self.danger:
            print("Danger Word!")
        else:
            print("Incorrect!")
        return False
        

    def isGameOver(self):
        return len(self.mywords) == 0 or self.danger in self.guesses

    