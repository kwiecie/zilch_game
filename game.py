from player import Player
from die import Die
import random
from collections import Counter

class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.current_roll_score = {}
        self.dices = []
        self.dices_to_reroll = []
        self.current_round = False
        self.last_round = False
        self.winner = None
        self.zilch = False

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
            self.dices[i] = random.randint(1,6)
        return self.dices


    '''def re_roll(self, dices_to_reroll):
        #Funkcja przerzucająca wybrane kości
        for dice in self.dices:
            if dice in dices_to_reroll:
                self.dices[dice] = random.randint(1,6)'''

        #for dice in dices_to_reroll:
        #    self.dices.append(random.randint(1,6))
            #rerolled_dice = random.randint(1, 6)
        #return self.dices

    def check_score(self):
        '''Dodać wszystkie możliwośći punktacji'''

        self.current_roll_score = {}
        one_score = 0
        two_score = 0
        three_score = 0
        four_score = 0
        five_score = 0
        six_score = 0
        strit_score = 0

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
        if one_score != 0:
            self.current_roll_score[1] = one_score

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
        if five_score != 0:
            self.current_roll_score[5] = five_score

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
        if two_score != 0:
            self.current_roll_score[2] = two_score

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
        if three_score != 0:
            self.current_roll_score[3] = three_score

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
        if four_score != 0:
            self.current_roll_score[4] = four_score

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
        if six_score != 0:
            self.current_roll_score[6] = six_score

        #wynik za strita
        if one == 1 and two == 1 and three == 1 and four == 1 and five ==1 and six == 1:
            strit_score = 1500
        if strit_score != 0:
            self.current_roll_score['strit'] = strit_score

        print('ile jedynek: %s, wynik za rzut: %s' % (one, one_score))
        print('ile dwójek: %s, wynik za rzut: %s' % (two, two_score))
        print('ile trójek: %s, wynik za rzut: %s' % (three, three_score))
        print('ile czwórek: %s, wynik za rzut: %s' % (four, four_score))
        print('ile piątek: %s, wynik za rzut: %s' % (five, five_score))
        print('ile szóstek: %s, wynik za rzut: %s' % (six, six_score))
        print('wynik za strit: %s' % strit_score)
        '''if self.current_roll_score:
            print(self.current_roll_score)
            #return self.current_roll_score
        else:
            print('Zilch!')
            self.zilch = True
            #self.current_roll_score = []
            #self.current_player.player.current_round_score = {}
            #return self.current_roll_score'''

        return self.current_roll_score

    def check_if_zilch(self):
        if self.current_roll_score == {}:
            self.zilch = True
        return self.zilch

    def remove_from_dices(self):
        pass

    def winner(self):
        if self.players[self.current_player].score >= 1000:
             self.winner == self.players[self.current_player]
        return self.winner

    def check_if_last_round(self):
        if self.players[self.current_player].winner == True:
            self.players[self.last_round] = True
        return self.last_round


    def check_winner(self):
        if self.players[self.current_player].winner == True:
            self.winner = self.players[self.current_player].winner
            return self.winner

    '''def add_to_bank(self):
        self.players[self.current_player].game_score.append(sum(self.players[self.current_player].round_scores))
        #zakończ turę sum(self.round_scores)
        #return self.score + self.round_scores[self.round_counter]
        return self.players[self.current_player].game_score'''

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