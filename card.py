from random import shuffle
class Card(object):


    def __init__(self,ranks,suits):
        self.ranks=ranks
        self.suits=suits
    def __str__(self):
        return "({} {})".format(self.ranks,self.suits)


class Desk(object):

    def __init__(self):
        Ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        SUITS = ["c", "d", "h", "s"]
        self.cards=[Card(r,s) for r in Ranks for s in SUITS]
        shuffle(self.cards)
