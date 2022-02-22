from die import Die

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_scores = []
        self.dices_saved = []
        self.dices_to_reroll = []
        self.current_round_score = []
        self.round_counter = 0
        self.winner = False

    def __repr__(self):
        return f'''
        Imię: {self.name}
        Wynik: {self.score}
        Runda: {self.round_counter}
        '''

    def get_name(self):
        return self.name

    def reset(self, dice_to_reset):
        dice_to_reset.clear()

        for i in range(6):
            dice_to_reset.append(Die())

        return dice_to_reset

    def play_turn(self):
        score = 0
        turn_ended = False
        dice = []

        while not turn_ended:
            if len(dice) == 0:
                dice = self.reset(dice)

            self.roll(dice)
            print("%s player rolles %s" % (self.name, dice))

    def roll(self, dice_to_roll):
        for die in dice_to_roll:
            die.roll()

    def add_to_reroll(self, index):
        print(self)
        dice = self.dices_saved.pop(index)
        self.dices_to_reroll.append(dice)

    def remove_from_reroll(self, index):
        dice = self.dices_to_reroll.pop(index)
        self.dices_saved.append(dice)

    def handle_reroll_by_array_index(self, index_list):
        dice_list = []
        for index in index_list:
            dice_list.append(self.dices_saved[index])

        new_dices_saved = [x for x in self.dices_saved if x not in dice_list]
        self.dices_to_reroll = dice_list
        self.dices_saved = new_dices_saved

    def sum_the_score(self):
        '''Sums the score of player'''
        self.score = sum(self.round_scores)
        return self.score

    def check_if_wins(self):
        if self.score >= 1000:
            self.winner = True
        return self.winner

    def add_to_bank(self):
        #zakończ turę
        #return self.score + self.round_scores[self.round_counter]
        pass
