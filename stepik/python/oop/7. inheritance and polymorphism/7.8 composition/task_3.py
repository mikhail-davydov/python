import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:

    def __init__(self):
        self.__suits = ("♣", "♢", "♡", "♠")
        self.__ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self.cards = [Card(suit, rank) for suit in self.__suits for rank in self.__ranks]

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError('Все карты разыграны')
        return self.cards.pop()

    def __str__(self):
        return f'Карт в колоде: {len(self.cards)}'
