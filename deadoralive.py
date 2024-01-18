import random
import time

items=['bear','handcuff','cigaratte','dagger','magnifier']
#class player
class player:
    def __init__(self):
        self.health=4
        self.playeritems=[]
    def __str__(self):
        return f'now you have 4 lives'
    def be_shot(self):
        self.health-=1
    def get_items(self):
        for i in range(1,5):
            random_items=random.choice(items)
            self.playeritems.append(random_items)
        return self.playeritems
    def delete_playeritems(self):
        self.playeritems=[]
        return self.playeritems
    def drink_bear(self):
        return f'has drank bear,one bullet out'
    def use_cigaratte(self):
        if self.health<4 and self.health>0:
            self.health+=1
    def handcuffed(self):
        return False
    def avoid(self):
        return f'Player has avoid'



    
#shotgun classs
    
class shotgun:
    def __init__(self):
        self.truebullet=random.randint(1,5)
        self.chamber=random.randint(5,7)
        self.falsebullet=self.chamber-self.truebullet
        self.bullet_in_chamber=random.randint(1,self.chamber)
    def __str__(self):
        return f'there are {self.truebullet} true bullets and {self.falsebullet} false bullets'
    
    def shoot(self):
        true_bullet_rate=range(1,self.truebullet+1)
        shot=self.bullet_in_chamber
        if shot in true_bullet_rate:
            self.truebullet-=1
            self.chamber-=1
            result= f'true bullet'
        else:
            self.falsebullet-=1
            self.chamber-=1
            result= f'false bullet'
        if self.chamber>0:
            self.bullet_in_chamber=random.randint(1,self.chamber)
        else:
            self.bullet_in_chamber=None
        return result
    def shake_chamber(self):
        self.truebullet=random.randint(1,5)
        self.chamber=random.randint(5,7)
        self.falsebullet=self.chamber-self.truebullet

    def used_magnifier(self):
        return f'The bullet in chamber is {self.bullet_in_chamber}'
    def drank_bear(self):
        self.shoot()
        return f'{self.bullet_in_chamber} has been ejected'
#Class used
running=True
Player1=player()
Player2=player()

#Game background description and rule explaination


print('welcome to dead or alive , no one leave before anyone of you die')
time.sleep(3)
print("Each of you have 4 lives to stay on this desk, no one leave until anyone of you die.")
print("You 2 will have round one by one,choose widly to shoot self or your opponent")
print("Each of you will have 4 items for helping you to defeat your enemy." )
print("Bear will eject the bullet already in the chamber")
print('Cigaratte will recover you 1 lives')
print('Handcuff will restrain your enemy for 1 round')
print('dagger will cut the shotgun barrel, you will cause 2 lives in one shot if bullet is true bullet')
print('Magnifier will discover the bullet in the chamber')
print('Once there are no bullets in chamber anymore, items will be refreshed')
time.sleep(5)
print('Ready?')
time.sleep(3)
print("Let's start")
time.sleep(2)
Shotgun=shotgun()

#main 

while running:
    player1_extra_rounds=0
    player2_extra_rounds=0
    rounds=Shotgun.chamber
    player_turn=random.randint(1,2)
    Player1items=Player1.get_items()
    Player2items=Player2.get_items()
    print(f'Player1 you have {Player1items}')

    print(f'Player2 you have {Player2items}')
    current_round=1
    #counting rounds
    handcuff_round=1
    Extra_round_player1=False # Check does player2 has been locked or not
    Extra_round_player2=False # Check does player1 has been locked or not
    while current_round<=rounds or Extra_round_player1 or Extra_round_player2 :
        print(f'current round is {current_round}')
        print(Shotgun)
        if player_turn==1:
            shoot=input(f'player1 your turn, you have{Player1items}')
            while shoot !='self' and shoot!='enemy' and shoot not in Player1items:
                shoot =input(f'Invalid input, please type again, self or enemy,or use items {Player1items} by type them')
        
            if shoot in Player1items:#检测是否有使用道具
                if shoot =='handcuff':#检测是否使用手铐
                    Player1items.remove(shoot)
                    print(f'Used handcuff,now you have {Player1items}')
                    Extra_round_player1=True#handcuffed player2
                    player_turn=1
                    continue
                else:
                    player_turn=2
                

            #Player1 action
            
            elif shoot == 'self':
                shoot=Shotgun.shoot()
                if shoot=='true bullet':#player1 shoot self, false bullet cintinue,true bullet change round
                    print('!!!!!!BANG!!!!!!')
                    Player1.be_shot()#player1 health-1
                    if Player1.health>0:
                        print(f'Player1 has been shot,player1 has {Player1.health} left')
                        if Extra_round_player1==True:
                            player_turn=1
                        else:
                            player_turn=2
                    else:
                        print(f'Player1 has dead, player2 has won. ')
                        running=False
                        break
                else:
                    print('!!!!!!DING!!!!!!')
                    print(f'Player1 has avoid , player1 has{Player1.health} left,cintinue to player1 round')
                    continue
            elif shoot=='enemy':
                shoot=Shotgun.shoot()
                if shoot=='true bullet':#decide player1 be shot or not
                    print('!!!!!!BANG!!!!!!')
                    Player2.be_shot()#player1 health-1
                    print(f'Player2 has been shot, player2 has {Player2.health} left')
                    player_turn=2
                    if Extra_round_player1 ==True:
                        player_turn=1
                else:
                    print('!!!!!!DING!!!!!!')
                    Player2.avoid()
                    print(f'Player2 has avoid , player2 has {Player2.health} left')
                    player_turn=2
        elif player_turn==2:
            shoot=input(f'player2 your turn, you have {Player2items}')
            while shoot !='self' and shoot!='enemy' and shoot not in Player2items:
                shoot =input(f'Invalid input, please type again, shoot self or enemy,you have {Player2items}')

            if shoot in Player2items:#检测是否有使用道具
                
                if shoot =='handcuff':#检测是否使用手铐
                    Player2items.remove(shoot)
                    print(f'Used handcuff,now you have {Player2items}')
                    Extra_round_player2=True
                    player_turn=2
                    continue
                else:
                    player_turn=1

            elif shoot == 'self':
                shoot=Shotgun.shoot()
                if shoot=='true bullet':#player2 shoot self, judge if player2 has been shot or not,if shot, change round
                    print('!!!!!!BANG!!!!!!')
                    Player2.be_shot()#player2 health-1
                    if Player2.health>0:
                        print(f'Player2 has been shot,player2 has {Player2.health} left')
                        player_turn=1
                        if Extra_round_player2==True:
                            player_turn=2
                    else:
                        print(f'Player2 has dead, player1 has won. ')
                        running=False
                        break

                else:
                    print('!!!!!!DING!!!!!!')
                    Player2.avoid()
                    print(f'Player2 has avoid , player2 has{Player2.health} left,continue to player2 round')
                    continue
            elif shoot=='enemy':#change round in both situation of TRUE and FALSE bullet 
                shoot=Shotgun.shoot()
                if shoot=='true bullet':#decide player1 be shot or not
                    print('!!!!!!BANG!!!!!!')
                    Player1.be_shot()#player1 health-1
                    if Player1.health>0:
                        print(f'Player1 has been shot,player1 has {Player1.health} left')
                        player_turn=1
                        if Extra_round_player2==True:
                            player_turn=2
                    else:
                        print(f'Player1 has dead, player2 has won. ')
                        running=False
                        break
                else:
                    Player1.avoid()
                    print('!!!!!!DING!!!!!!')
                    print(f'Player1 has avoid , player1 has {Player1.health} left')
                    player_turn=1
                    if Extra_round_player2==True:
                        player_turn=2
        current_round+=1    
        if player_turn==1 and (Extra_round_player1 and player1_extra_rounds<=2):
            player1_extra_rounds+=1
            
    
        elif player_turn==2 and (Extra_round_player2 and player2_extra_rounds<=2):
            player2_extra_rounds+=1
            
        else:
            Extra_round_player1=False
            Extra_round_player2=False

    if Player1.health ==0 or Player2.health ==0:
        running=False
        break
    Shotgun.shake_chamber()#Fresh chamber
    time.sleep(2)
    print(f'Round over')
    time.sleep(2)
    print(f'Player1 has ',end='')
    time.sleep(2)
    print(Player1.health,'lives')
    time.sleep(2)
    print('Player2 has ',end='')
    time.sleep(2)
    print(Player2.health,'lives')
    time.sleep(2)
    print('new round begin')
    time.sleep(2)
time.sleep(2)
print('GAME OVER!!')

   

                


        


