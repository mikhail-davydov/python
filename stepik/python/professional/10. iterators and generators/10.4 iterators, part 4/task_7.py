class CardDeck:
    def __init__(self):
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.suits = ["пик", "треф", "бубен", "червей"]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= 52:
            raise StopIteration
        cards_idx, suits_idx = self.idx % len(self.cards), self.idx // len(self.cards)
        self.idx += 1
        return f'{self.cards[cards_idx]} {self.suits[suits_idx]}'


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])


# alt
class CardDeck:
    def __init__(self):
        suit = ('пик', 'треф', 'бубен', 'червей')
        number = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.deck = (f'{j} {i}' for i in suit for j in number)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.deck)


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
