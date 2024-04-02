import random

class Player:

    def __init__(self,team):
        self.name=self.generate_name()
        self.skill=random.random()
        self.team=team
        self.pitching=random.random()
        self.batting=random.random()
        self.running=random.random()
        self.hair=random.random()+0.1
        

    def generate_name(self):
        first = open('./firstNames').read().splitlines()
        last = open('./lastNames').read().splitlines()
        return(str(random.choice(first)+' '+random.choice(last)))


    def run(self):
        return (random.randrange(0,12)*self.running)+self.hair < 5
    
    def get_pitching(self):
        return str(f"{self.pitching:.1f}")

    def get_batting(self):
        return str(f"{self.batting:.1f}")
    
    def get_running(self):
        return str(f"{self.running:.1f}")

    def check_hair(self):
        if self.hair > 0.7:
            return 'Their hair looks GLORIOUS. '
        elif self.hair > 0.6:
            return 'Their hair looks great. '
        elif self.hair > 0.5:
            return 'Their hair looks good. '
        elif self.hair > 0.4:
            return 'Their hair is fine. '
        elif self.hair > 0.3:
            return 'They\'ve seen better days. '
        elif self.hair > 0.2:
            return 'They have let go of themselves. '
        elif self.hair > 0.2:
            return 'I can\'t believe they stepped outside looking like that. '
        else:
            return 'They look like shit. '