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

# Helpers
def reset_bases():
    g.half_inning()

def average_pbr(team):
    average_p=0
    average_b=0
    average_r=0
    for x in range(TEAMSIZE):
        average_p+=team[x].pitching
        average_b+=team[x].batting
        average_r+=team[x].running
    return 'P: '+str(f"{average_p/TEAMSIZE:.2f}")+'| B: '+str(f"{average_b/TEAMSIZE:.2f}")+'| R: '+str(f"{average_r/TEAMSIZE:.2f}")


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
print('Home Team\t\tAverage PBR - '+ average_pbr(homeTeam))
print('---------\n')

for x in range(TEAMSIZE):
    if(len(homeTeam[x].name) < 16):
        print(homeTeam[x].name+'\t\t\tP: '+homeTeam[x].get_pitching()+'| B: '+homeTeam[x].get_batting()+'| R: '+homeTeam[x].get_running())
    else:
        print(homeTeam[x].name+'\t\tP: '+homeTeam[x].get_pitching()+'| B: '+homeTeam[x].get_batting()+'| R: '+homeTeam[x].get_running())

input('\n\n\tPress Enter for Away Team\n')
os.system('cls')

print('Away Team\t\tAverage PBR - '+ average_pbr(awayTeam))
print('---------\n')
for x in range(TEAMSIZE):
    if(len(homeTeam[x].name) < 16):
        print(awayTeam[x].name+'\t\t\tP: '+awayTeam[x].get_pitching()+' B: '+awayTeam[x].get_batting()+' R: '+awayTeam[x].get_running())
    else:
        print(awayTeam[x].name+'\t\tP: '+awayTeam[x].get_pitching()+' B: '+awayTeam[x].get_batting()+' R: '+awayTeam[x].get_running())

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
        print(awayTeam[awayBatter].name + ' is up. '+awayTeam[awayBatter].check_hair())
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
        print(homeTeam[homeBatter].name + ' is up. '+homeTeam[homeBatter].check_hair())
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

    
