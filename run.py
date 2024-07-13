import argparse
import logging
import sys

from game import Game
from glove_decoder import GloVeDecoder
from glove_encoder import GloVeEncoder

import gensim.downloader as api

import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

glove = api.load("glove-wiki-gigaword-100")

def parse_args():
    parser = argparse.ArgumentParser(description="Run automatic operative and spymaster for Codenames.")
    parser.add_argument('--save', type=int, default=1, help='Whether to save')
    parser.add_argument('--epochs', type=int, default=1, help='Number of iterations')
    parser.add_argument('--candidates', type=int, default=20, help='Number of candidates')
    parser.add_argument('--verbose', type=int, default=1, help='Verbose Setting')
    parser.add_argument('--append', type=int, default=0, help='Append Setting')
    parser.add_argument('--negatives', type=int, default=20, help='Number of negatives')
    parser.add_argument('--good', type=int, default=9, help='Number of good words')
    return parser.parse_args()


def main():
    args = parse_args()
    
    decoder = GloVeDecoder(glove)
    encoder = GloVeEncoder(decoder, glove, n_candidates=args.candidates, n_negative_samples=args.negatives)
    history = []
    if args.append > 0:
        with open("history.json", "r") as f: 
            history = json.load(f)

    for it in range(args.epochs):
        print(f"------ Epoch {it + 1} / {args.epochs} ------")
        game = Game(encoder, decoder, glove=glove, n_words=25, n_good_words=args.good, verbose=args.verbose)
        history.append(game.startGame())
        del game

    if args.save > 0:
        with open("history.json", "w") as f:
            json.dump(history , f)
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
