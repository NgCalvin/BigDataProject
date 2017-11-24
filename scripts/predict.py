import os
import sys

import pandas as pd

from text_preprocessor import TextPreprocessor
from predictor import Predictor, ShingleScore

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Predict score a text.')
    parser.add_argument('--text', metavar='Text',
                        help='the text to be predicted')
    parser.add_argument('--database', metavar='Database', required=True,
                        help='the database file for prediction')
    parser.add_argument('--shingle-length', metavar='ShingleLength', type=int,
                        help='the shingle length the predictor focus on')

    args = parser.parse_args()

    return args

def predict(text_preprocessor, predictor, text):
    processed_text = text_preprocessor.process(text)
    return predictor.predict(processed_text)

if __name__ == '__main__':
    args = parse_args()

    database_file = args.database
    if not os.path.exists(database_file):
        print("Cannot find database file \"{}\"".format(database_file),
              file=sys.stderr)
        exit(2)

    predictor = Predictor(shingle_len_filter=args.shingle_length)
    df = pd.read_csv(database_file)
    for idx, r in df.iterrows():
        shingle_score = ShingleScore(shingle=r['shingle'],
                                     score=r['score'],
                                     frequency=r['frequency'])
        predictor.addShingleScore(shingle_score)

    tp = TextPreprocessor()

    input_text = args.text
    if input_text is not None and len(input_text) > 0
        text = argv.pop()
        score = predict(tp, predictor, input_text)
        print("Score = {}".format(score))
        exit()

    # interactive mode
    text = None
    while text is None or len(text.strip()) == 0:
        try:
            text = input('predict> ')
            score = predict(tp, predictor, text)
            print("Score = {}".format(score))
        except (EOFError, KeyboardInterrupt):
            print()
            exit()

        text = None
