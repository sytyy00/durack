from random import shuffle
from random import randint

RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
SUITS = ['♠', '♦', '♥', '♣']


class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.weight = WEIGHT[self.ranks]
        self.trump = False

    def __repr__(self):#вывод карты
        return "({} {} {} {})".format(self.ranks, self.suits, self.weight, self.trump)


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

    def deal_card(self):#выдача карты из колоды
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Hand:
    def __init__(self):
        self.cards = []

    def get_hand(self):#возвращает список карт в руке
        return self.cards

    def __str__(self):#вывод руки
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "None"
        return rep

    def add(self, card):#добавление карты в руку
        if card != None:
            self.cards.append(card)

    def give(self, card, other_hand):#передача карты из руки в другую
        self.cards.remove(card)
        other_hand.add(card)

    def sort(self):#сортировка руки
        self.cards.sort(key=lambda x: (x.trump, x.weight))


class Game():
    def __init__(self):
        self.d = Desk()
        self.e = Enemy()
        self.p = Player()
        self.my_hand = Hand()
        self.other_hand = Hand()
        self.table = Hand()
        for i in range(6):
            self.my_hand.add(self.d.deal_card())
            self.other_hand.add(self.d.deal_card())
        self.my_hand.sort()
        self.other_hand.sort()
        print("Your hand")
        print("#" * 100)
        print(self.my_hand)
        print(self.other_hand)

    def attacker(self):  # 0, атака игрока ,защита бота
        step = None
        my_card = self.p.player_step(self.my_hand.get_hand())
        while True:
            self.my_hand.give(my_card, self.table)
            print()
            print("TABLE")
            print(self.table)
            print("#" * 100)
            other_card = self.e.enemy_repel(self.table.get_hand()[0], self.other_hand.get_hand())
            if other_card != None:
                self.other_hand.give(other_card, self.table)
                print(self.table)
                print("#" * 100)

                step = 1
            else:

                step = 0
                for i in range(len(self.table.get_hand())):
                    #self.table.give(self.table.get_hand()[i], self.other_hand)
                    self.other_hand.add(self.table.get_hand()[i])
                break
            print("Your hand")
            print()
            print(self.my_hand)
            my_card = self.p.toss(self.table.get_hand(), self.my_hand.get_hand())
            if my_card == None:
                break
        if step == 1:
            print()
            print("Successful defense")
        else:
            print("To abandon the defense")

        self.table.get_hand().clear()

        return step

    def defender(self):  # 1, атака бота, защита игрока
        step = None
        other_card = self.e.enemy_step(self.other_hand.get_hand())
        while True:
            self.other_hand.give(other_card, self.table)
            print()
            print("TABLE")
            print(self.table)
            print("#" * 100)
            my_card = self.p.player_repel(self.table.get_hand()[0], self.my_hand.get_hand())
            if my_card != None:
                self.my_hand.give(my_card, self.table)
                print(self.table)
                print("#" * 100)

                step = 0
            else:

                step = 1
                for i in range(len(self.table.get_hand())):
                    #self.table.give(self.table.get_hand()[i], self.my_hand)
                    self.my_hand.add(self.table.get_hand()[i])
                break
            print("Your hand")
            print()
            print(self.my_hand)
            other_card = self.e.toss(self.table.get_hand(), self.other_hand.get_hand())
            if other_card == None:
                break
        if step == 0:
            print()
            print("Successful defense")
        else:
            print("To abandon the defense")

        self.table.get_hand().clear()

        return step

    def trump(self):#метод узнаёт ,кто ходит первым по козырям
        attack = None
        other = self.e.enemy_trump(self.other_hand.get_hand())
        me = self.p.player_trump(self.my_hand.get_hand())
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

    def refill(self):#пополнение рук
        if len(self.my_hand.get_hand()) < 6:
            for i in range(6 - len(self.my_hand.get_hand())):
                self.my_hand.add(self.d.deal_card())
        if len(self.other_hand.get_hand()) < 6:
            for i in range(6 - len(self.other_hand.get_hand())):
                self.other_hand.add(self.d.deal_card())
        self.my_hand.sort()
        self.other_hand.sort()
        print("Your hand")
        print("#" * 100)
        print(self.my_hand)


class Enemy():  # 1
    def enemy_step(self, hand):#ход бота
        return hand[0]

    def enemy_repel(self, card, hand):#защита бота
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

    def enemy_trump(self, hand):#козыри бота для того,чтобы узнать ,кто ходит первым
        card = None
        for i in range(len(hand)):
            if hand[i].trump:
                card = hand[i]
                break
        return card

    def toss(self,table,hand):#бот подкидывает карты ,если есть такая возможность
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
    def player_step(self, hand):#ход игрока
        in_card = int(input("Strike "))
        return hand[in_card - 1]

    def player_repel(self, card, hand):#защита игрока
        print("Press 9 to pass")
        car_rep = None
        while True:
            in_card = int(input("Repel "))
            if in_card == 9:
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

    def player_trump(self, hand):#козырь игрока
        card = None
        for i in range(len(hand)):
            if hand[i].trump:
                card = hand[i]
                break
        return card

    def toss(self,table,hand):#подкинуть карту
        tab = []
        exitFlag = False
        car_toss = None
        print("Press 9 to pass")
        for i in range(len(table)):
            tab.append(table[i].weight)
        while True:
            in_card = int(input("Toss "))
            if in_card == 9:
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
        return car_toss






game = Game()#сама игра
step = game.trump()
while True:
    if step == 1:
        step = game.defender()
        game.refill()
    elif step == 0:
        step = game.attacker()
        game.refill()
