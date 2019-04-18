import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(_card):
    rank_value = FrenchDeck.ranks.index(_card.rank)
    return rank_value * len(suit_value) + suit_value[_card.suit]


deck = FrenchDeck()
for card in sorted(deck, key=spades_high):
    print(card)

print(len(deck))
print(deck[0])
print(random.choice(deck))
print(deck[:3])
print(deck[12::13])
