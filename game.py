import random
import math
import player

class Game:
    def __init__(self):
        self.outcomes=['hit','strike, looking','strike, swinging','foul','ball']
        self.balls=0
        self.strikes=0
        self.player_outs=0
        self.out=False
        self.away_score=0
        self.home_score=0
        self.on_base=False
        self.bases={
            "first":None,
            "second":None,
            "third":None,
        }

    def check_balls(self):
        return self.balls

    def check_strikes(self):
        return self.strikes
    
    def check_out(self):
        return self.out
    
    def check_onbase(self):
        return self.on_base
    
    def players_out(self):
        return self.player_outs

    def end_at_bat(self):
        self.balls=0
        self.strikes=0
        self.out=False
        self.on_base=False

    def half_inning(self):
        self.player_outs=0
        self.bases={
            "first":None,
            "second":None,
            "third":None,
        }

    def advance_bases(self):
        print('\tadvance_bases')
        if self.bases['third']!= None:
            self.out=self.bases['third'].run()
            if self.out:
                print(self.bases['third'].name + ' is out at 3rd.')
            else:
                print(self.bases['third'].name + ' made it home!')
                if self.bases['third'].team=='away':
                    self.away_score=self.away_score+1
                else:
                    self.home_score=self.home_score+1
            self.bases['third']=None

        if self.bases['second']!= None:
            self.out=self.bases['second'].run()
            if self.out:
                print(self.bases['second'].name + ' is out at 2nd.')
            else:
                print(self.bases['second'].name + ' made it to third base.')
            
            self.bases['third']=self.bases['second']
            self.bases['second']= None

        if self.bases['first']!= None:
            self.out=self.bases['first'].run()
            if self.out:
                print(self.bases['first'].name + ' is out at 1st.')
            else:
                print(self.bases['first'].name + ' made it to second base.')
            
            self.bases['second']=self.bases['first']
            self.bases['first']= None

    def hit(self,player):
        print('\thit')
        x= math.floor(random.randrange(0,5)+player.skill)
        self.advance_bases()
        match x:
            case 0:
                self.out=True
                self.player_outs=self.player_outs+1
                return 'HIT... ground out.'
            case 1:
                self.out=True
                self.player_outs=self.player_outs+1
                return 'HIT!! ....but caught out'
            case 2:
                player.on_base=1
                self.on_base=True
                self.bases['first']=player
                return 'BASE HIT!!'
            case 3:
                player.on_base=2
                self.on_base=True
                self.bases['second']=player
                return 'IT\'S A DOUBLE!'
            case 4:
                player.on_base=3
                self.on_base=True
                self.bases['third']=player
                return 'IT\'S A TRIPLE!'
            case 5:
                self.on_base=True
                if player.team=='away':
                    self.away_score=self.away_score+1
                else:
                    self.home_score=self.home_score+1
                return 'HOME RUN!!'

    def ball(self, player):
        print('\tball')
        pitch=random.randrange(0,5)
        match pitch:
            case 0:
                return self.hit(player) 
            case 1:
                self.strikes=self.strikes+1
                if self.strikes == 3:
                    self.player_outs=self.player_outs+1
                return self.outcomes[1]
            case 2:
                self.strikes=self.strikes+1
                if self.strikes == 3:
                    self.player_outs=self.player_outs+1
                return self.outcomes[2]
            case 3:
                if self.strikes < 2:
                    self.balls=self.balls+1
                return self.outcomes[3]
            case 4:
                self.balls=self.balls+1
                if self.balls==4:
                    self.on_base=True
                return self.outcomes[4]
            


