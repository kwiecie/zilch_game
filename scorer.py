from collections import Counter

class Score:

    '''def __init__(self):
        self.score = 0
        self.num_of_diced_used = 0

    def __str__(self):
        return "%s:%s" % (self.score, self.num_of_diced_used)

    def __repr__(self):
        return "%s:%s" % (self.score, self.num_of_diced_used)'''
    @staticmethod
    def score(dice_list):
        occurences = Counter(sorted(dice_list))
        most_common = occurences.most_common(6)

        if most_common[0][1] == 6:
            '''Six of a kind'''
            return most_common[0][0] * 800

        if most_common[0][1] == 5:
            '''Five of a kind'''
            return most_common[0][0] * 400

        if most_common[0][1] == 4:
            '''Four of a kind'''
            return most_common[0][0] * 200

        if most_common[0][1] == 3:
            '''Three of a kind'''
            return most_common[0][0] * 100

    def __str__(self):
        return "%s" % (self.score)

    def __repr__(self):
        return "%s" % (self.score)

class Scorer:
    def score(self, dice):
        if type(dice) == set or type(dice) == dict:
            return self.score(list(dice))

        kind_of_a_score = self.Score()
        value_count = [0] * 6

        for die in dice:
            if die is not None:
                value_count[die.get_value() - 1] += 1

    def score_one_of_a_kind(self, value):
        # 1 = 100 points
        # 5 = 50 points
        score = self.Score()

        if value == 1:
            score.score = 100
        elif value == 5:
            score.score = 50

        score.number_of_dice_used = 1
        return score

    def score_two_of_a_kind(self, value):
        # No special scoring for doubles so score each die separately
        score = self.Score()

        score.score = self.score_one_of_a_kind(value).score * 2
        if score.score > 0:
            score.number_of_dice_used = 2
        else:
            score.number_of_dice_used = 0

        return score

    def score_three_of_a_kind(self, value):
        score = self.Score()

        # Any triple = number x 100 points
        # The exception is when you have three 1’s = 1000 points
        if value == 1:
            score.score = 1000
        else:
            score.score = value * 100

        if score.score > 0:
            score.number_of_dice_used = 3
        else:
            score.number_of_dice_used = 0

        return score

    def score123456(self, value_count):
        # 123456 = 2000 points
        score = self.Score()
        one_of_each = True

        for value in value_count:
            if value != 1:
                one_of_each = False

        if one_of_each:
            score.score = 2000
            score.number_of_dice_used = 6

        return score