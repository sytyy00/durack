from random import shuffle


class Card:
    def __init__(self, ranks, suits,weight,trump):
        self.ranks = ranks
        self.suits = suits
        self.weight = weight
        self.trump = trump
    def __repr__(self):
        return "({} {} {} {})".format(self.ranks, self.suits,self.weight,self.trump)


class Desk:
    def __init__(self):
        self.cards = []
        RANKS = ['6','7','8','9','10','J','Q','K',"A"]
        WEIGHT = {"6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13,"A":14}
        SUITS = ["c", "d", "h", "s"]
        for i in range(len(SUITS)):
            s = SUITS[i]
            for j in range(len(RANKS)):
                r = RANKS[j]
                w = WEIGHT[r]
                t = False
                self.cards.append(Card(r,s,w,t))
        shuffle(self.cards)
        m = self.cards[0].suits
        for i in range(len(self.cards)):
            if m == self.cards[i].suits:
                self.cards[i].trump = True
    def deal_card(self):
        if len(self.cards)>0:
            return self.cards.pop()
        else:return None

class Hand:
    def __init__(self):
        self.cards = []
    def value(self):
        return self.cards
    def __str__(self):
        if self.cards:
            rep =""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "None"
        return rep
    def add(self,card):
        if card != None:
            self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Game():
    def __init__(self):
        d = Desk()
        self.my_hand = Hand()
        self.other_hand = Hand()
        self.table = Hand()
        for i in range(36):
            self.my_hand.add(d.deal_card())
            #self.other_hand.add(d.deal_card())
        print(self.my_hand)

    def strike(self):
        in_card = int(input("Strike "))
        s = len(self.my_hand.value())
        print(s)
        self.my_hand.give(self.my_hand.value()[in_card-1],self.table)
        print(self.table)
        print(self.my_hand)




#class Enemy():

game =Game()
game.strike()














