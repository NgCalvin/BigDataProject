import os
import sys

import pandas as pd

from text_preprocessor import TextPreprocessor

if __name__ == '__main__':
    if len(sys.argv) != 3:
        try:
            script_name = sys.argv[0]
        except IndexError:
            script_name = 'preprocess.py'
        print('Usage: python {} <InputFile> <OutputFile>'.format(script_name),
              file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    tp = TextPreprocessor()
    data = pd.read_csv(input_file)[['Score', 'Text']]

    def action(row):
        row['Text'] = tp.process(row['Text'])
        return row

    data.apply(action, axis=1).to_csv(output_file,
                                      index=False,
                                      index_label=False)
