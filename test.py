import unittest
from card import Card, RANKS, SUITS, WEIGHT, Hand, Desk, Enemy


class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card(RANKS[0], SUITS[0])

    def test_init(self):
        self.assertEqual(self.card.suits, SUITS[0])
        self.assertEqual(self.card.weight, WEIGHT[RANKS[0]])
        self.assertEqual(self.card.ranks, RANKS[0])
        self.assertEqual(self.card.trump, False)

    def test_display(self):
        self.assertEqual(self.card.__repr__(), "({} {})".format(RANKS[0], SUITS[0]))


class HandTest(unittest.TestCase):
    def setUp(self):
        self.card = []
        self.cards = Card(RANKS[1], SUITS[1])
        self.card.append(Card(RANKS[0], SUITS[0]))
        self.card.append(Card(RANKS[1], SUITS[1]))
        self.hand_1 = Hand()
        self.hand = Hand()
        self.hand.add(Card(RANKS[0], SUITS[0]))
        self.hand.add(Card(RANKS[1], SUITS[1]))

    def test_get_hand(self):
        self.assertEqual(self.hand.get_hand()[0], self.card[0])

    def test_str(self):
        self.assertEqual(self.hand.__str__(), '(6 ♠)  (7 ♦)  \n')

    def test_add(self):
        self.assertIsNone(self.hand.add(Card(RANKS[2], SUITS[2])))

    def test_give(self):
        self.assertEqual(self.hand.give(self.hand.get_hand()[0], self.hand_1),None)
        #self.hand.get_hand()[0] is not self.hand.get_hand()


class LogicTest(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy()
        self.hand = Hand()
        self.card = Card(RANKS[0], SUITS[0])
        self.card.trump = True
        self.hand.add(self.card)
        self.hand.add(Card(RANKS[1], SUITS[1]))
        self.table = Hand()
        self.table.add(Card(RANKS[1], SUITS[3]))

    def test_step(self):
        self.assertEqual(self.enemy.enemy_step(self.hand.get_hand()), self.hand.get_hand()[0])

    def test_trump(self):
        self.assertEqual(self.enemy.enemy_trump(self.hand.get_hand()), self.hand.get_hand()[0])

    def test_repel(self):
        self.assertEqual(self.enemy.enemy_repel(Card(RANKS[2], SUITS[2]), self.hand.get_hand()),
                         self.hand.get_hand()[0])

    def test_tos(self):
        self.assertEqual(self.enemy.toss(self.table.get_hand(), self.hand.get_hand()), self.hand.get_hand()[1])


if __name__ == "__main__":
    unittest.main()
