from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from random import randint

from player import Player
from game import Game
from scorer import Score

app = Flask(__name__)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board')
def board():
    global game
    return render_template('board.html', game = game, current_player = game.players[game.current_player])

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/solo')
def solo():
    return render_template('solo.html')

@app.route('/solo_start', methods=['POST'])
def solo_start():
    global game
    game = Game()
    for player in request.form:
        if request.form[player] != '':
            game.add_player(request.form[player])
    game.set_dices()
    if game.num_of_players() <= 1:
        return redirect('/solo')
    else:
        return redirect('/board')


'''
@app.route('/roll', methods=['POST'])
def roll():
    global game
    if game.num_of_players() == 0:
        return redirect('/solo')
    print(game.players)
    #print(game.players[0].dices_saved)
    print(game.current_player)
    to_reroll = []

    if 'd1' in request.form:
        to_reroll.append(0)
    if 'd2' in request.form:
        to_reroll.append(1)
    if 'd3' in request.form:
        to_reroll.append(2)
    if 'd4' in request.form:
        to_reroll.append(3)
    if 'd5' in request.form:
        to_reroll.append(4)
    if 'd6' in request.form:
        to_reroll.append(5)
    print(to_reroll)
    #if 'd1' in request.form:
    #    player.dices_saved.append(0)
    #if 'd2' in request.form:
    #    player.dices_saved.append(1)
    #if 'd3' in request.form:
    #    player.dices_saved.append(2)
    #if 'd4' in request.form:
    #    player.dices_saved.append(3)
    #if 'd5' in request.form:
    #    player.dices_saved.append(4)
    #if 'd6' in request.form:
    #    player.dices_saved.append(5)

    #game.players[game.current_player].handle_reroll_by_array_index(to_reroll)
    game.roll(to_reroll)

    if game.check_if_last_round():
        return redirect('/win')

    return redirect('/board')
'''

@app.route('/roll', methods=['POST', 'GET'])
def roll():
    global game
    score = Score()
    print('number of players: ')
    print(game.num_of_players())
    if game.num_of_players() == 0:
        return redirect('/solo')

    to_reroll = []
    if 'd1' in request.form:
        to_reroll.append(0)
    if 'd2' in request.form:
        to_reroll.append(1)
    if 'd3' in request.form:
        to_reroll.append(2)
    if 'd4' in request.form:
        to_reroll.append(3)
    if 'd5' in request.form:
        to_reroll.append(4)
    if 'd6' in request.form:
        to_reroll.append(5)

    print('dices to reroll: ')
    print(to_reroll)
    #game.players[game.current_player].handle_reroll_by_array_index(to_reroll)
    game.re_roll(to_reroll)
    print(game.dices)
    #print(game.check_score())


    #if game.check_if_finished():
    #    return redirect('/win')

    return redirect('/board')

@app.route('/save_dices')
def save_dices():
    #game.players[game.current_player].current_round_score = 0
    score = game.check_score()
    game.players[game.current_player].round_scores.append(score)

    return redirect('/board')

@app.route('/bank', methods=['POST', 'GET'])
def bank():
    #game.players[game.current_player].round_scores += game.players[game.current_player].current_round_score
    print(game.players[game.current_player])
    game.players[game.current_player].round_counter += 1
    game.players[game.current_player].add_to_bank()
    game.next_player()
    game.reset_dices()
    game.set_dices()
    return redirect('/board')

@app.route('/win')
def win():
    global WINNER
    return render_template('win.html', winner=WINNER)

def check():
    return False

if __name__ == '__main__':
    app.run(debug=True)
