import os
import sys

import pandas as pd

from text_preprocessor import TextPreprocessor
from predictor import Predictor, ShingleScore

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2 or argc > 4:
        try:
            script_name = sys.argv[0]
        except IndexError:
            script_name = 'predict.py'
        print('Usage: python {} <DataBaseFile> [Text]'.format(script_name),
              file=sys.stderr)
        exit(1)

    database_file = sys.argv[1]
    if not os.path.exists(database_file):
        print("Cannot find database file \"{}\"".format(database_file),
              file=sys.stderr)
        exit(2)
    df = pd.read_csv(database_file)

    predictor = Predictor()
    for idx, r in df.iterrows():
        shingle_score = ShingleScore(shingle=r['Shingle'],
                                     score=r['Score'],
                                     frequency=r['Frequency'])
        predictor.addShingleScore(shingle_score)

    tp = TextPreprocessor()
    def predict(text):
        processed_text = tp.process(text)
        return predictor.predict(processed_text)

    if argc == 3:
        text = sys.argv[2]
        score = predict(text)
        print("Score = {}".format(score))
        exit(0)

    # interactive mode
    text = None
    while text is None or len(text.strip()) == 0:
        try:
            text = input('predict> ')
            score = predict(text)
            print("Score = {}".format(score))
        except (EOFError, KeyboardInterrupt):
            print()
            exit(0)

        text = None
