import os
import sys

import pandas as pd

from text_preprocessor import TextPreprocessor
from predictor import Predictor, ShingleScore, UniformPredictor

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Predict score a text.')
    parser.add_argument('--text', metavar='Text',
                        help='the text to be predicted')
    parser.add_argument('--database', metavar='Database', required=True,
                        help='the database file for prediction')
    parser.add_argument('--shingle-length', metavar='ShingleLength', type=int,
                        help='the shingle length the predictor focus on')

    group = parser.add_argument_group(
        title='Ensemble Mode',
        description='Ensemble mode uses multiple predictors to '
                    'predict the score of a text.'
    )
    group.add_argument('--ensemble-mode', action='store_true', default=False,
                       help='enable ensemble mode')
    group.add_argument('--coefficient', metavar='Coefficient',
                       help='coefficient file used for ensemble the '
                            'predictors. (Required for Ensemble Mode)')

    args = parser.parse_args()

    if args.ensemble_mode and args.coefficient is None:
        parser.error('--coefficient is required for ensemble mode')

    return args

def simple_predict(text_preprocessor, predictor, text):
    processed_text = text_preprocessor.process(text)
    return predictor.predict(processed_text)

def ensemble_predict(text_preprocessor, predictors, coefficients, text):
    processed_text = text_preprocessor.process(text)
    final_score = 0
    for idx in range(min(len(predictors), len(coefficients))):
        score = predictors[idx].predict(processed_text)
        final_score += coefficients[idx] * score
    return final_score

if __name__ == '__main__':
    args = parse_args()

    database_file = args.database
    if not os.path.exists(database_file):
        print("Cannot find database file \"{}\"".format(database_file),
              file=sys.stderr)
        exit(2)

    db = pd.read_csv(database_file)
    tp = TextPreprocessor()
    predict = None
    if args.ensemble_mode:
        coefficient_file = args.coefficient
        if not os.path.exists(coefficient_file):
            print('Cannot find coefficient file "{}"'.format(coefficient_file),
                  file=sys.stderr)
            exit(3)

        coefficients = []
        with open(coefficient_file) as c_file:
            line = c_file.readline()
            while len(line) != 0:
                stripped = line.rstrip('\n').strip()
                if len(stripped) > 0:
                    coeff = float(stripped)
                    coefficients.append(coeff)
                line = c_file.readline()

        predictors = [ UniformPredictor(value=1) ]
        for idx in range(1, len(coefficients)):
            predictors.append(Predictor(shingle_len_filter=idx))

        for idx, r in db.iterrows():
            shingle_score = ShingleScore(shingle=r['shingle'],
                                         score=r['score'],
                                         frequency=r['frequency'])

            for predictor in predictors:
                predictor.addShingleScore(shingle_score)

        def predict(text):
            return ensemble_predict(tp, predictors, coefficients, text)

    else:
        predictor = Predictor(shingle_len_filter=args.shingle_length)
        for idx, r in db.iterrows():
            shingle_score = ShingleScore(shingle=r['shingle'],
                                         score=r['score'],
                                         frequency=r['frequency'])
            predictor.addShingleScore(shingle_score)

        def predict(text):
            return simple_predict(tp, predictor, text)

    input_text = args.text
    if input_text is not None and len(input_text) > 0:
        score = predict(input_text)
        print("Score = {}\n".format(score))
        exit()

    # interactive mode
    text = None
    while text is None or len(text.strip()) == 0:
        try:
            text = input('predict> ')
            score = predict(text)
            print("Score = {}\n".format(score))
        except (EOFError, KeyboardInterrupt):
            print()
            exit()

        text = None
