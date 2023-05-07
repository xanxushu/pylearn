#this is a poke game code!
import random
import math

#this is the card class ,which is the mix of number and color.
class card():
    #to create a kind of card
    def __init__(self,cardcolor,cardnum):
        self.cardnum=cardnum
        self.cardcolor=cardcolor
    #a NUM and a COLOR , the value of the card,52 in total
    NUM=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    COLOR=["♠","♥","♣","♦"]
    #give every card a order
    def cardorder(self):
        if self.cardcolor=="♠":
            colororder=0
        if self.cardcolor=="♥":
            colororder=1
        if self.cardcolor=="♣":
            colororder=2
        if self.cardcolor=="♦":
            colororder=3
        if self.cardnum=="A":
            numorder=1
        if self.cardnum=="J":
            numorder=11
        if self.cardnum=="Q":
            numorder=12
        if self.cardnum=="K":
            numorder=13
        if int(self.cardnum) in range(2,11):
            numorder=int(self.cardnum)
        return colororder*13+numorder
    def __str__(self):
        rep=self.cardcolor+self.cardnum
        return rep

#this is class hand,which is the players in the game
class hand():
    def __init__(self):
        self.hold=[] #hold is the cards that the player owns
    def __str__(self):#show all the cards that the player holds
        if self.hold:
            rep=""
            for card in self.hold:
                rep+=str(card)+" "
        else:
            rep="the player has no poke in hand"
        return rep
    def clearhold(self):#the number of cards that the player holds turn to 0
        self.hold=[]
    def addhold(self,card):#add cards to the player
        self.hold.append(card)
    def outhold(self,card):#put out a card that the player holds
        self.hold.remove(card)
    def give(self,card,player):
        self.hold.remove(card)
        player.addhold

#this is class poke,which is the main of the game including poke itself and the rules
class poke(hand):
    def a_pair_poke(self):
        for color in card.COLOR:
            for num in card.NUM:
                self.addhold(card(color,num))
    def mixcard(self):
        random.shuffle(self.hold)
    def gamestart(self,hands,once):
        for times in range(once):
            for hand in hands:
                if self.hold:
                    topcard=self.hold[0]
                    self.hold.remove(topcard)
                    hand.addhold(topcard)
                else:
                    print("there is no poke that could be arranged")


print("there are four players in this game,everyone holds 13 pokes")
poke1=poke()
poke1.a_pair_poke()
poke1.mixcard()
players=[hand(),hand(),hand(),hand()]
j=1
for hand in players:
    print("player%d:"%j)
    print(hand)
    j+=1
poke1.gamestart(players,13)
n=1
for hand in players:
    print("player%d:"%n,end="")
    print(hand)
    n+=1