import random
import math
import player

class Game:
    def __init__(self):
        self.outcomes=['hit','Strike, looking.','Strike, swinging.','Foul','Ball']
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
    def print_gamestate(self,team):
        OUTS=['','X','X X','X X X']
        bases=[' ',' ',' ']
        bases[0] = ' ' if self.bases['first']==None else 'X'
        bases[1] = ' ' if self.bases['second']==None else 'X'
        bases[2] = ' ' if self.bases['third']==None else 'X'

        print('__________________')
        print('        _')
        print('       |'+bases[1]+'|')
        print('    _       _')
        print('   |'+bases[2]+'|     |'+bases[0]+'|')
        print('------------------')
        print('OUT: '+OUTS[self.players_out()])
        match team:
            case 'away':
                print('Home - '+ str(self.home_score) +'  '+ str(self.away_score)+' - AWAY')
            case 'home':
                print('HOME - '+ str(self.home_score) +'  '+ str(self.away_score)+' - Away')
        print('------------------')

    def advance_bases(self):
        #print('\tadvance_bases')
        message=''
        if self.bases['third']!= None:
            self.out=self.bases['third'].run()
            if self.out:
                message+=self.bases['third'].name + ' is out at 3rd. '
            else:
                message+=self.bases['third'].name + ' made it home! '
                if self.bases['third'].team=='away':
                    self.away_score=self.away_score+1
                else:
                    self.home_score=self.home_score+1
            self.bases['third']=None

        if self.bases['second']!= None:
            self.out=self.bases['second'].run()
            if self.out:
                message+=self.bases['second'].name + ' is out at 2nd. '
            else:
                message+=self.bases['second'].name + ' made it to third base.'
                self.bases['third']=self.bases['second']
            self.bases['second']= None

        if self.bases['first']!= None:
            self.out=self.bases['first'].run()
            if self.out:
                message+=self.bases['first'].name + ' is out at 1st. '
            else:
                message+=self.bases['first'].name + ' made it to second base. '
                self.bases['second']=self.bases['first']
            self.bases['first']= None
        return message

    def hit(self,player):
        #print('\thit')
        message=''
        x= math.floor(random.randrange(0,5)+player.skill)
        match x:
            case 0:
                self.out=True
                self.player_outs=self.player_outs+1
                if self.player_outs <3:
                    message=self.advance_bases()
                return 'HIT... ground out. '+message
 
            case 1:
                self.out=True
                self.player_outs=self.player_outs+1
                return 'HIT!! ....but caught out. '
            case 2:
                message=self.advance_bases()

                self.on_base=True
                self.bases['first']=player
                return 'BASE HIT!! '+message
            case 3:
                message=self.advance_bases()
                self.on_base=True
                self.bases['second']=player
                return 'Hit for a DOUBLE! '+message
            case 4:
                message=self.advance_bases()
                self.on_base=True
                self.bases['third']=player
                return 'Hit for a TRIPLE! '+message
            case 5:
                message=self.advance_bases()
                self.on_base=True
                if player.team=='away':
                    self.away_score=self.away_score+1
                else:
                    self.home_score=self.home_score+1
                return 'HOME RUN!! '+message

    def walk(self, player):
        if self.bases['first'] == None:
            self.bases['first'] = player
            return str('\n'+self.bases['first'].name + ' walks to first.')
        elif self.bases['second'] == None:
            self.bases['second'] = self.bases['first']
            self.bases['first'] = player
            return str('\n'+self.bases['first'].name + ' walks to first. \n'+self.bases['second'].name+ ' walks to second.')
        elif self.bases['third'] == None:
            self.bases['third'] = self.bases['second']
            self.bases['second'] = self.bases['first']
            self.bases['first'] = player

            return str('\n'+self.bases['first'].name + ' walks to first. \n'+self.bases['second'].name+ ' walks to second. \n'+self.bases['second'].name + ' walks to third.')
  
        else:
            match str(self.bases['third'].team):
                case 'home':
                    self.home_score+=1
                case 'away':
                    self.away_score+=1
            old_third =self.bases['third'].name
            self.bases['third'] = self.bases['second']
            self.bases['second'] = self.bases['first']
            self.bases['first'] = player
            self.bases['first'].on_base=1
            self.bases['second'].on_base = 2
            self.bases['third'].on_base = 3
            return str('\n'+old_third + 'walks home!\n'+self.bases['first'].name + ' walks to first. \n'+self.bases['second'].name+ ' walks to second. \n'+self.bases['second'].name + ' walks to third.')

    def pitch(self, player):
        message=''
        #print('\tball')
        #['hit','strike, looking','strike, swinging','foul','ball']
        pitch=random.randrange(0,5)
        match pitch:
            case 0:
                return self.hit(player) 
            case 1:
                self.strikes=self.strikes+1
                message=' '+str(self.balls)+' - '+str(self.strikes)
                if self.strikes == 3:
                    self.player_outs=self.player_outs+1
                    message='\n'+player.name+' is OUT'
                return self.outcomes[1]+message
            case 2:
                self.strikes=self.strikes+1
                message=' '+str(self.balls)+' - '+str(self.strikes)
                if self.strikes == 3:
                    self.player_outs=self.player_outs+1
                    message='\n'+player.name+' is OUT'
                return self.outcomes[2]+message
            case 3:
                
                if self.strikes < 2:
                    self.strikes+=1
                message=' '+str(self.balls)+' - '+str(self.strikes)
                return self.outcomes[3]+message
            case 4:
                self.balls=self.balls+1
                message=' '+str(self.balls)+' - '+str(self.strikes)
                if self.balls==4:
                    self.on_base=True
                    message=self.walk(player)
                return self.outcomes[4]+message
                
                

            


