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
        self.bases=[None,None,None,None]

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

    def base_numbers(self,number):
        match number:
            case 1:
                return 'first'
            case 2:
                return 'second'
            case 3:
                return 'third'


    def half_inning(self):
        self.player_outs=0
        self.bases=[None,None,None,None]

    def print_gamestate(self,team):
        OUTS=['','X','X X','X X X']
        bases=[None,' ',' ',' ']
        bases[1] = ' ' if self.bases[1]==None else 'X'
        bases[2] = ' ' if self.bases[2]==None else 'X'
        bases[3] = ' ' if self.bases[3]==None else 'X'

        print('__________________')
        print('        _')
        print('       |'+bases[2]+'|')
        print('    _       _')
        print('   |'+bases[3]+'|     |'+bases[1]+'|')
        print('------------------')
        print('OUT: '+OUTS[self.players_out()])
        match team:
            case 'away':
                print('Home - '+ str(self.home_score) +'  '+ str(self.away_score)+' - AWAY')
            case 'home':
                print('HOME - '+ str(self.home_score) +'  '+ str(self.away_score)+' - Away')
        print('------------------')

    def advance_bases(self,mod):
        #print('\tadvance_bases')
        message=''

        if mod > 1:
            for x in range(len(self.bases)-1,-1,-1):
                if self.bases[x]!= None:
                    if x+mod < 4:
                        self.bases[x+mod] = self.bases[x]
                        message+=self.bases[x].name + ' made it to '+str(self.base_numbers(x+mod))+'. '
                        self.bases[x]=None
                    else:
                        message+=self.bases[x].name+ ' made it home! '
                        if self.bases[x].team=='away':
                            self.away_score=self.away_score+1
                        else:
                            self.home_score=self.home_score+1
                        self.bases[x]=None
        else:
            for x in range(len(self.bases)-1,-1,-1):
                if self.bases[x]!= None:
                    if self.bases[x].run:
                        if x+mod < 4:
                            self.bases[x+mod] = self.bases[x]
                            self.bases[x]=None
                        else:
                            message+=self.bases[x].name+ ' made it home! '
                            if self.bases[x].team=='away':
                                self.away_score=self.away_score+1
                            else:
                                self.home_score=self.home_score+1
                            self.bases[x]=None
                    else:
                        message+=self.bases[x].name+' is out at'+str(self.base_numbers(x))+'. '
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
                    message=self.advance_bases(1)
                return 'HIT... ground out. '+message
 
            case 1:
                self.out=True
                self.player_outs=self.player_outs+1
                return 'HIT!! ....but caught out. '
            case 2:
                message=self.advance_bases(1)
                self.on_base=True
                self.bases[1]=player
                return 'BASE HIT!! '+player.name+' made it to first. '+message
            case 3:
                message=self.advance_bases(2)
                self.on_base=True
                self.bases[2]=player
                return 'Hit for a DOUBLE! '+message
            case 4:
                message=self.advance_bases(3)
                self.on_base=True
                self.bases[3]=player
                return 'Hit for a TRIPLE! '+message
            case 5:
                message=self.advance_bases(3)
                self.on_base=True
                if player.team=='away':
                    self.away_score=self.away_score+1
                else:
                    self.home_score=self.home_score+1
                return 'HOME RUN!! '+message

    def walk(self, player):
        self.bases[0]=None
        if self.bases[1] == None:
            self.bases[1] = player
            return str('\n'+self.bases[1].name + ' walks to first.')
        elif self.bases[2] == None:
            self.bases[2] = self.bases[1]
            self.bases[1] = player
            return str('\n'+self.bases[1].name + ' walks to first. \n'+self.bases[2].name+ ' walks to second.')
        elif self.bases[3] == None:
            self.bases[3] = self.bases[2]
            self.bases[2] = self.bases[1]
            self.bases[1] = player

            return str('\n'+self.bases[1].name + ' walks to first. \n'+self.bases[2].name+ ' walks to second. \n'+self.bases[2].name + ' walks to third.')
  
        else:
            match str(self.bases[3].team):
                case 'home':
                    self.home_score+=1
                case 'away':
                    self.away_score+=1
            old_third =self.bases[3].name
            self.bases[3] = self.bases[2]
            self.bases[2] = self.bases[1]
            self.bases[1] = player
            self.bases[1].on_base=1
            self.bases[2].on_base = 2
            self.bases[3].on_base = 3
            return str('\n'+old_third + 'walks home!\n'+self.bases[1].name + ' walks to first. \n'+self.bases[2].name+ ' walks to second. \n'+self.bases[2].name + ' walks to third.')

    def pitch(self, player):
        message=''
        self.bases[0]=player
        #print('\tpitch')
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
                
                

            


