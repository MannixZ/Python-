import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')

deck = FrenchDeck()
print(len(deck))  # 类对象也可以用 len 方法，是因为该类实现了 __len__ 函数

from random import choice

print(deck[:3])
print(choice(deck))  # 类可以使用切片，随机抽取数，相当于一个迭代器，是因为实现了 __getitem__ 方法
