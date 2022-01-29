from player import Player
from die import Die
import random
from collections import Counter

class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.dices = []
        self.dices_to_reroll = []
        self.current_round = False
        self.last_round = False
        self.winner = -1

    def add_player(self, name):
        self.players.append(Player(name))

    def delete_player(self):
        self.players.pop()

    def num_of_players(self):
        return len(self.players)

    def next_player(self):
        if self.current_round:
            self.current_player += 1
            self.current_player %= self.num_of_players()

    def set_dices(self):
        '''Generuje kości na początku gry'''
        for dice in range(1, 7):
            self.dices.append(random.randint(1, 6))
        return self.dices

    def roll(self, dice_list):
        for i in range(len(dice_list)):
            random_dice = random.randint(1, 6)
            print(random_dice)
            #self.players[self.current_player].dices_saved.append(random_dice)

    def re_roll(self, dices_to_reroll):
        '''Funkcja przerzucająca wybrane kości'''
        for dice in self.dices:
            if dice in dices_to_reroll:
                self.dices[dice] = random.randint(1,6)

        #for dice in dices_to_reroll:
        #    self.dices.append(random.randint(1,6))
            #rerolled_dice = random.randint(1, 6)
        return self.dices

    def check_score(self):
        score = 0
        Counter(self.dices)
        if 1 in self.dices:
            score = 100
        elif 5 in self.dices:
            score = 50
        #elif Counter(self.dices)
        return score

    def check_if_last_round(self):
        if self.last_round == 1:
            return self.winner


    def __repr__(self):
        return  f'''
                lista graczy: {str(self.players)}
                aktywny gracz: {repr(self.current_player)}
                dices: {self.dices}
                '''
'''
    def check_if_last_round(self):
        if self.current_player >= 1000:
            self.last_round = True
            self.winner = self.current_player

        return self.winner
'''