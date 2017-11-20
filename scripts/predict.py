import os
import sys

import pandas as pd

from text_preprocessor import TextPreprocessor
from predictor import Predictor, ShingleScore

if __name__ == '__main__':
    argv = sys.argv.copy()
    argv.reverse()

    argc = len(argv)
    if argc < 2 or argc > 5:
        try:
            script_name = argv[-1]
        except IndexError:
            script_name = 'predict.py'
        print('Usage: python {} <DatabaseFile> [ShingleLength] [Text]'.format(script_name),
              file=sys.stderr)
        exit(1)
    else:
        argv.pop()

    database_file = argv.pop()
    if not os.path.exists(database_file):
        print("Cannot find database file \"{}\"".format(database_file),
              file=sys.stderr)
        exit(2)

    shingle_length = None
    if len(argv) != 0:
        shingle_length_str = argv.pop()
        try:
            shingle_length = int(shingle_length_str)
        except (ValueError, TypeError):
            argv.append(shingle_length_str)

    predictor = Predictor(shingle_length)
    df = pd.read_csv(database_file)
    for idx, r in df.iterrows():
        shingle_score = ShingleScore(shingle=r['shingle'],
                                     score=r['score'],
                                     frequency=r['frequency'])
        predictor.addShingleScore(shingle_score)

    tp = TextPreprocessor()
    def predict(text):
        processed_text = tp.process(text)
        return predictor.predict(processed_text)

    if len(argv) != 0:
        text = argv.pop()
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
