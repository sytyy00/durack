from random import shuffle


class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits

    def __str__(self):
        return "({} {})".format(self.ranks, self.suits)


class Desk:
    def __init__(self):
        Ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        SUITS = ["c", "d", "h", "s"]
        self.cards = [Card(r, s) for r in Ranks for s in SUITS]
        shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()

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
    def give(self,card):
        self.cards.append(card)



