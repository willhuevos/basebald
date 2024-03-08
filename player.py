import random

class Player:

    def __init__(self,team):
        self.name=self.generate_name()
        self.skill=random.random()
        self.on_base=0
        self.team=team

    def generate_name(self):
        first = open('./firstNames').read().splitlines()
        last = open('./lastNames').read().splitlines()
        return(str(random.choice(first)+' '+random.choice(last)))


    def run(self):
        return random.randrange(0,12)< 5