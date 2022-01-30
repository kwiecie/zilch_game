from player import Player
from die import Die
import random
from collections import Counter

class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0
        #.current_round_score = 0
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
        self.current_player += 1
        self.current_player %= self.num_of_players()
        self.players[self.current_player].round_counter += 1

    def set_dices(self):
        '''Generuje kości na początku gry'''
        for dice in range(1, 7):
            self.dices.append(random.randint(1, 6))
        return self.dices

    def reset_dices(self):
        self.dices = []
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
        '''Dodać wszystkie możliwośći punktacji'''
        one_score = 0
        two_score = 0
        three_score = 0
        four_score = 0
        five_score = 0
        six_score = 0

        self.players[self.current_player].current_round_score = 0
        #dices_counter = sorted(Counter(self.dices))
        def count_one_kind(lst, kind):
            return self.dices.count(kind)

        one = count_one_kind(self.dices, 1)
        if one == 6:
            one_score = 8000
        elif one == 5:
            one_score = 4000
        elif one == 4:
            one_score = 2000
        elif one == 3:
            one_score = 1000
        elif one == 2:
            one_score = 200
        elif one == 1:
            one_score = 100
        else:
            one_score = 0

        five = count_one_kind(self.dices, 5)
        if five == 6:
            five_score = 4000
        elif five == 5:
            five_score = 2000
        elif five == 4:
            five_score = 1000
        elif five == 3:
            five_score = 500
        elif five == 2:
            five_score = 100
        elif five == 1:
            five_score = 50
        else:
            five_score = 0

        #wynik za dwójki
        two = count_one_kind(self.dices, 2)
        if two == 6:
            two_score = 1600
        elif two == 5:
            two_score = 800
        elif two == 4:
            two_score = 400
        elif two == 3:
            two_score = 200
        else:
            two_score = 0

        # wynik za trójki
        three = count_one_kind(self.dices, 3)
        if three == 6:
            three_score = 2400
        elif three == 5:
            three_score = 1200
        elif three == 4:
            three_score = 600
        elif three == 3:
            three_score = 300
        else:
            three_score = 0

        # wynik za czwórki
        four = count_one_kind(self.dices, 4)
        if four == 6:
            four_score = 3200
        elif four == 5:
            four_score = 1600
        elif four == 4:
            four_score = 800
        elif four == 3:
            four_score = 400
        else:
            four_score = 0

        # wynik za szóstki
        six = count_one_kind(self.dices, 6)
        if six == 6:
            six_score = 4800
        elif six == 5:
            six_score = 2400
        elif six == 4:
            six_score = 1200
        elif six == 3:
            six_score = 600
        else:
            six_score = 0

        print('ile jedynek: %s, wynik za rzut: %s' % (one, one_score))
        print('ile dwójek: %s, wynik za rzut: %s' % (two, two_score))
        print('ile trójek: %s, wynik za rzut: %s' % (three, three_score))
        print('ile czwórek: %s, wynik za rzut: %s' % (four, four_score))
        print('ile piątek: %s, wynik za rzut: %s' % (five, five_score))
        print('ile szóstek: %s, wynik za rzut: %s' % (six, six_score))
        #print('counter: ')
        #print(dices_counter)

        '''for dice in dices_counter:
            if dices_counter[1] == 6:
                score = 8000
            elif dices_counter[1] == 5:
                score = 4000
            elif dices_counter[1] == 4:
                score = 2000
            elif dices_counter[1] == 3:
                score = 1000
            elif dices_counter[1] == 2:
                score = 200
            elif dices_counter[1] == 1:
                score = 100
            else:
                score = 0'''
        #if 1 in self.dices:
        #    score = 100
        #elif 5 in self.dices:
        #    score = 50
        #else:
        #    score = 0
        #    print('Zilch!')
        #elif Counter(self.dices)

        #def add_to_round_score(self):
        #    game.players[game.current_player].sum_the_score()
        if one_score == five_score == 0:
            score = 0
        elif one_score >= five_score:
            score = one_score
        else:
            score = five_score

        return score

    def remove_from_dices(self):
        pass


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