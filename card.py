from random import shuffle


class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
    def __str__(self):
        return "({} {})".format(self.ranks, self.suits)


class Desk:
    def __init__(self):
        Ranks = ["A", "6", "7", "8", "9", "10", "J", "Q", "K"]
        SUITS = ["c", "d", "h", "s"]
        self.cards = [Card(r, s) for r in Ranks for s in SUITS]
        shuffle(self.cards)
    def deal_card(self):
        if len(self.cards)>0:
            return self.cards.pop()
        else:return None

class Hand:
    def __init__(self):
        self.cards = []
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
        for i in range(6):
            self.my_hand.add(d.deal_card())
            self.other_hand.add(d.deal_card())
        print(self.my_hand)

    def Strike(self):
        in_card = input("Strike ")
        print(self.my_hand)




#class Enemy():



















