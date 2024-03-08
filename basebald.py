# Baseball game

import math
import teamgen
import game

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
    for x in range(TEAMSIZE):
        homeTeam[x].on_base=0
        awayTeam[x].on_base=0
        g.half_inning()

# Introduce Game
print('\t\t---------')
print('\t\tBASEBALL!')
print('\t\t---------\n')
print('Home Team\t\t\tAway Team')
print('---------\t\t\t---------')
print()
for x in range(TEAMSIZE):
    if(len(homeTeam[x].name) < 16):
        print(homeTeam[x].name+'\t\t\t'+awayTeam[x].name)
    else:
        print(homeTeam[x].name+'\t\t'+awayTeam[x].name)

# PLAY BALL!
for inning in range(INNINGS):
    print('\nInning ' + str(inning+1))
    print('---------')
    print('Home - '+ str(g.home_score) +'  '+ str(g.away_score)+' - Away\n')

    print('Away team at the plate.\n')
    while g.players_out() < OUTS:
        # print('balls='+str(g.check_balls())+'strikes='+ str(g.check_strikes())+'onbase='+str(g.check_onbase())+'outs='+str(g.players_out()))
        while g.check_balls() < 4 and g.check_strikes() < 3 and not g.check_out() and not g.check_onbase():
            print(awayTeam[awayBatter].name + ' '+ g.ball(awayTeam[awayBatter]))
        g.end_at_bat()
        awayBatter=awayBatter+1
        if awayBatter > TEAMSIZE-1:
            awayBatter=0
    reset_bases()
    
    print('\nHome team at the plate.\n')
    while g.players_out() < OUTS:
        while g.check_balls() < 4 and g.check_strikes() < 3 and not g.check_out() and not g.check_onbase():
            print(homeTeam[homeBatter].name + ' '+ g.ball(homeTeam[homeBatter]))
        g.end_at_bat()
        homeBatter=homeBatter+1
        if homeBatter > TEAMSIZE-1:
            homeBatter=0
    reset_bases()
    print('End of inning!\n')

    
