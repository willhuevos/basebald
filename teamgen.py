# Generate Teams 
import player

TEAMSIZE=9

def generate_team(team):
    fullteam=[]
    for x in range(TEAMSIZE):
        fullteam.append(player.Player(team))
    return fullteam



