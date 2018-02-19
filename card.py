from random import shuffle
from random import randint
from log import game_logger, error

RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
SUITS = ['♠', '♦', '♥', '♣']


class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.weight = WEIGHT[self.ranks]
        self.trump = False

    def __repr__(self):
        """Output card"""
        return "({} {})".format(self.ranks, self.suits)


class Desk:
    def __init__(self):
        self.cards = []
        self.cards = [Card(r, s) for r in RANKS for s in SUITS]
        shuffle(self.cards)
        m = self.cards[0].suits
        print("Trump")
        print(self.cards[0])
        print()
        for i in range(len(self.cards)):
            if m == self.cards[i].suits:
                self.cards[i].trump = True

    def deal_card(self):
        """Issuance of cards from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Hand:
    def __init__(self):
        self.cards = []

    def get_hand(self):
        """Returns a list of cards in hand"""
        return self.cards

    def __str__(self):
        """Arm output"""
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "None"
        rep += "\n"
        return rep

    def add(self, card):
        """Adding a card to the hand"""
        if card != None:
            self.cards.append(card)

    def give(self, card, other_hand):
        """From the hand of the card transfer to another"""
        self.cards.remove(card)
        other_hand.add(card)

    def sort(self):
        """Hand sorting"""
        self.cards.sort(key=lambda x: (x.trump, x.weight))


class Game():
    def __init__(self):
        self.desk = Desk()
        self.enemy = Enemy()
        self.player = Player()
        self.my_hand = Hand()
        self.other_hand = Hand()
        self.table = Hand()
        for i in range(6):
            self.my_hand.add(self.desk.deal_card())
            self.other_hand.add(self.desk.deal_card())
        self.my_hand.sort()
        self.other_hand.sort()
        print("Your hand")
        print("#" * 100)
        print(self.my_hand)

    def attacker(self):
        """0, player attack, bot protection"""
        step = None
        my_card = self.player.player_step(self.my_hand.get_hand())
        s = 0
        while True:
            self.my_hand.give(my_card, self.table)
            #print()
            print("TABLE")
            print(self.table)
            print("#" * 100)
            other_card = self.enemy.enemy_repel(self.table.get_hand()[s], self.other_hand.get_hand())
            if other_card != None:
                self.other_hand.give(other_card, self.table)
                print(self.table)
                print("#" * 100)

                step = 1
            else:

                step = 0
                for i in range(len(self.table.get_hand())):
                    # self.table.give(self.table.get_hand()[i], self.other_hand)
                    self.other_hand.add(self.table.get_hand()[i])
                break
            print("Your hand")
            print(self.my_hand)
            my_card = self.player.toss(self.table.get_hand(), self.my_hand.get_hand())
            if my_card == None:
                break
            s = s + 2
        if step == 1:
            #print()
            print("Successful defense")
        else:
            print("To abandon the defense")

        self.table.get_hand().clear()

        return step

    def defender(self):
        """1, bot attack, player protection"""
        step = None
        other_card = self.enemy.enemy_step(self.other_hand.get_hand())
        s = 0
        while True:
            self.other_hand.give(other_card, self.table)
            #print()
            print("TABLE")
            print(self.table)
            print("#" * 100)
            my_card = self.player.player_repel(self.table.get_hand()[s], self.my_hand.get_hand())
            if my_card != None:
                self.my_hand.give(my_card, self.table)
                print(self.table)
                print("#" * 100)

                step = 0
            else:

                step = 1
                for i in range(len(self.table.get_hand())):
                    # self.table.give(self.table.get_hand()[i], self.my_hand)
                    self.my_hand.add(self.table.get_hand()[i])
                break
            print("Your hand")
            print(self.my_hand)
            other_card = self.enemy.toss(self.table.get_hand(), self.other_hand.get_hand())
            if other_card == None:
                break
            s = s + 2
        if step == 0:
            #print()
            print("Successful defense")
        else:
            print("To abandon the defense")

        self.table.get_hand().clear()

        return step

    def trump(self):
        """Method finds out who goes first of trumps"""
        attack = None
        other = self.enemy.enemy_trump(self.other_hand.get_hand())
        me = self.player.player_trump(self.my_hand.get_hand())
        if other == None and me != None:
            attack = 0
        else:
            if other != None and me == None:
                attack = 1
            else:
                if other == None and me == None:
                    attack = randint(0, 1)
                else:
                    if other.weight < me.weight:
                        attack = 1
                    else:
                        attack = 0
        return attack

    def refill(self):
        """Hand replenishment"""
        m = None
        other_len = len(self.other_hand.get_hand())
        my_len = len(self.my_hand.get_hand())
        if my_len < 6:
            for i in range(6 - my_len):
                self.my_hand.add(self.desk.deal_card())
        if other_len < 6:
            for i in range(6 - other_len):
                self.other_hand.add(self.desk.deal_card())
        self.my_hand.sort()
        self.other_hand.sort()
        print("Your hand")
        print("#" * 100)
        print(self.my_hand)
        if my_len == 0:
            m = 0
        if other_len == 0:
            m = 1
        return m

    def number_card(self):
        while True:
            try:
                in_card = int(input("Strike "))
                return in_card
            except ValueError:
                error.exception("Exception message")



class Enemy():  # 1
    def enemy_step(self, hand):
        """Bot step"""
        return hand[0]

    def enemy_repel(self, card, hand):
        """Bot protection"""
        car_rep = None
        for i in range(len(hand)):
            if card.suits == hand[i].suits and card.weight < hand[i].weight:
                car_rep = hand[i]
                break
        if car_rep == None:
            for i in range(len(hand)):
                if hand[i].trump:
                    if not card.trump:
                        car_rep = hand[i]
                        break
                    elif card.trump and card.weight < hand[i].weight:
                        car_rep = hand[i]
                        break
        return car_rep

    def enemy_trump(self, hand):
        """The trump cards of the bot in order to find out who is the first to go"""
        card = None
        for i in range(len(hand)):
            if hand[i].trump:
                card = hand[i]
                break
        return card

    def toss(self, table, hand):
        """The bot throws cards, if there is such an opportunity"""
        tab = []
        exitFlag = False
        car_toss = None
        for i in range(len(table)):
            tab.append(table[i].weight)
        for i in range(len(tab)):
            m = tab[i]
            for j in range(len(hand)):
                if m == hand[j].weight:
                    car_toss = hand[j]
                    exitFlag = True
                    break
            if exitFlag:
                break
        return car_toss


class Player():  # 0
    def player_step(self, hand):
        """Player step"""
        while True:
            in_card = game.number_card()
            if in_card <= len(hand):
                return hand[in_card - 1]

            else:
                print("Fail")

    def player_repel(self, card, hand):
        """Player protection"""
        print("Press 0 to pass")
        car_rep = None
        while True:
            in_card = game.number_card()
            if in_card <= len(hand):
                if in_card == 0:
                    break
                if card.suits == hand[in_card - 1].suits and card.weight < hand[in_card - 1].weight:
                    car_rep = hand[in_card - 1]
                    break
                if hand[in_card - 1].trump:
                    if not card.trump:
                        car_rep = hand[in_card - 1]
                        break
                    elif card.trump and card.weight < hand[in_card - 1].weight:
                        car_rep = hand[in_card - 1]
                        break
                else:
                    print("Fail")
        return car_rep

    def player_trump(self, hand):
        """Player's trump card"""
        card = None
        for i in range(len(hand)):
            if hand[i].trump:
                card = hand[i]
                break
        return card

    def toss(self, table, hand):
        """Toss card"""
        tab = []
        exitFlag = False
        car_toss = None
        print("Press 0 to pass")
        for i in range(len(table)):
            tab.append(table[i].weight)
        while True:
            in_card = int(input("Toss "))
            if in_card <= len(hand):
                if in_card == 0:
                    break
                else:
                    for i in range(len(tab)):
                        m = tab[i]
                        if m == hand[in_card - 1].weight:
                            car_toss = hand[in_card - 1]
                            exitFlag = True
                            break
                    if exitFlag:
                        break
            else:
                print("Fail")
        return car_toss


"""The game itself"""
game = Game()
step = game.trump()
m = None
game_logger.info("Start game")
while True:
    if step == 1:
        step = game.defender()
        m = game.refill()
        if m == 1:
            print("Win bot")
            game_logger.info("win bot")
            break
        if m == 0:
            print("Win player")
            game_logger.info("win player")
            break

    elif step == 0:
        step = game.attacker()
        m = game.refill()
        if m == 1:
            print("Win bot")
            game_logger.info("win bot")
            break
        if m == 0:
            print("Win player")
            game_logger.info("win player")
            break
game_logger.info("Game end")
