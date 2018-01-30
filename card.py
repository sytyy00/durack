from random import shuffle

RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
SUITS = ["c", "d", "h", "s"]


class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.weight = WEIGHT[self.ranks]
        self.trump = False

    def __repr__(self):
        return "({} {} {} {})".format(self.ranks, self.suits, self.weight, self.trump)


class Desk:
    def __init__(self):
        self.cards = []
        self.cards = [Card(r, s) for r in RANKS for s in SUITS]
        shuffle(self.cards)
        m = self.cards[0].suits

        for i in range(len(self.cards)):
            if m == self.cards[i].suits:
                self.cards[i].trump = True

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Hand:
    def __init__(self):
        self.cards = []

    def get_hand(self):
        return self.cards

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "None"
        return rep

    def add(self, card):
        if card != None:
            self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Game():
    def __init__(self):
        d = Desk()
        e = Enemy()
        self.my_hand = Hand()
        self.other_hand = Hand()
        self.table = Hand()
        for i in range(6):
            self.my_hand.add(d.deal_card())
            self.other_hand.add(d.deal_card())
        print(self.my_hand)
        print(self.other_hand)

    def strike(self):
        in_card = int(input("Strike "))
        s = len(self.my_hand.get_hand())
        print(s)
        self.my_hand.give(self.my_hand.get_hand()[in_card - 1], self.table)
        print(self.table)
        print(self.my_hand)


class Enemy():
    def enemy_step(self, hand):
        card = hand[0]
        for i in range(len(hand)):
            if card.weight > hand[i].weight:
                card = hand[i]
        return card

    def enemy_repel(self, card, hand):
        car_rep = None
        for i in range(len(hand)):
            if card.suits == hand[i].suits:
                if card.weight < hand[i].weight:
                    car_rep = hand[i]
        if car_rep == None:
            for i in range(len(hand)):
                if hand[i].tump == True:
                    if card.trump == True and card.weight < hand[i].weight:
                        car_rep = hand[i]
                    elif card.trump == False:
                        car_rep = hand[i]
                        break
        return car_rep


game = Game()
game.strike()
