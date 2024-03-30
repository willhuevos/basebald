# Baseball game

import math
import teamgen
import game
import time
import os

# Constants
INNINGS=9
TEAMSIZE=9
OUTS=3

# Create Game
g = game.Game()

# Generate Teams
homeTeam=teamgen.generate_team('home')
awayTeam=teamgen.generate_team('away')

# Counters
homeBatter=0
awayBatter=0
out=False

# Helpers
def reset_bases():
    g.half_inning()

def print_end_stats():
    print('GAME OVER!')
    print('------------------')
    print('    Final Score:')
    print('Home - '+ str(g.home_score) +'  '+ str(g.away_score)+' - Away\n')
    if g.home_score > g.away_score:
        print('    Home Team Wins!!')
    else:
        print('    Away Team Wins!!')

# Introduce Game
print('\t\t---------')
print('\t\tBASEBALD!')
print('\t\t---------\n')
print('Home Team\t\t\tAway Team')
print('---------\t\t\t---------')
print()
for x in range(TEAMSIZE):
    if(len(homeTeam[x].name) < 16):
        print(homeTeam[x].name+'\t\t\t'+awayTeam[x].name)
    else:
        print(homeTeam[x].name+'\t\t'+awayTeam[x].name)

input('\n\n\tPress a key to Start...\n')
os.system('cls')

# PLAY BALL!
for inning in range(INNINGS):
    print('Inning ' + str(inning+1))
    print('---------')
    print('Home - '+ str(g.home_score) +'  '+ str(g.away_score)+' - Away\n')

    # AWAY LOGIC*******************************
    print('Away team at the plate.\n')
    time.sleep(3)
    os.system('cls')

    while g.players_out() < OUTS:
        print(awayTeam[awayBatter].name + ' is up.')
        time.sleep(2)

        while g.check_balls() < 4 and g.check_strikes() < 3 and not g.check_out() and not g.check_onbase():
            print(g.pitch(awayTeam[awayBatter]))
            time.sleep(1)

        g.end_at_bat()

        if g.players_out() < OUTS:
            g.print_gamestate('away')

        awayBatter=awayBatter+1

        if awayBatter > TEAMSIZE-1:
            awayBatter=0

        time.sleep(4)
        os.system('cls')

    reset_bases()

    # HOME LOGIC*******************************
    print('Home team at the plate.\n')
    time.sleep(3)
    os.system('cls')

    while g.players_out() < OUTS:
        print(homeTeam[homeBatter].name + ' is up.')
        time.sleep(2)

        while g.check_balls() < 4 and g.check_strikes() < 3 and not g.check_out() and not g.check_onbase():
            print(g.pitch(homeTeam[homeBatter]))
            time.sleep(1)

        g.end_at_bat()

        if g.players_out() < OUTS:
            g.print_gamestate('home')

        homeBatter=homeBatter+1

        if homeBatter > TEAMSIZE-1:
            homeBatter=0

        time.sleep(4)
        os.system('cls')

    reset_bases()

    if inning < 8:
        print('End of inning '+str(inning+1)+'!\n')
        print('Home - '+ str(g.home_score) +'  '+ str(g.away_score)+' - Away\n')
        input('Press a key to continue...\n')
        os.system('cls')
    else:
        print_end_stats()

    
