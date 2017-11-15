import sys

from collections import namedtuple

ShingleScore = namedtuple('ShingleScore', ['shingle', 'score', 'frequency'])

class Predictor:
    def __init__(self, shingle_len_filter = None):
        self.database = {}
        self.shingle_count = 0
        self.shingle_score_average = 0
        self.max_shingle_length = 0
        self.shingle_len_filter = shingle_len_filter

    def addShingleScore(self, shingle_score):
        shingle = shingle_score.shingle
        shingle_len = len(shingle.split(' '))

        if self.shingle_len_filter and self.shingle_len_filter != shingle_len:
            # filter the shingle length
            return

        shingle_scores = self.database.get(shingle, [])
        shingle_scores.append(shingle_score)
        self.database[shingle] = shingle_scores

        self.shingle_score_average = \
            (self.shingle_score_average * self.shingle_count + \
                shingle_score.score) / (self.shingle_count + 1)
        self.shingle_count += 1
        self.max_shingle_length = max(self.max_shingle_length, shingle_len)

    def predict(self, text):
        words = text.split(' ')
        word_count = len(words)

        score_dict = {}
        shingle_length_bound = min(self.max_shingle_length, word_count)
        for shingle_len in range(1, shingle_length_bound + 1):
            scores = []
            for idx in range(word_count - shingle_len + 1):
                shingle = ' '.join(words[idx : idx + shingle_len])
                shingle_scores = self.database.get(shingle, None)
                if shingle_scores:
                    scores.extend(shingle_scores)
            if len(scores) > 0:
                weighted_sum = 0
                weight = 0
                for each_score in scores:
                    weight += each_score.frequency
                    weighted_sum += each_score.score * each_score.frequency
                score_dict[shingle_len] = weighted_sum / weight

        if len(score_dict) == 0:
            print("Warning: Not enough shingles to predict", file=sys.stderr)
            return self.shingle_score_average

        score_sum = 0
        for shingle_len, score in score_dict.items():
            score_sum += score
        return score_sum / len(score_dict)
