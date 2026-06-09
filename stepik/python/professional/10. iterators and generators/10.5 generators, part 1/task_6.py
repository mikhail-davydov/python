def card_deck(suit):
    cards = [f'{j} {i}' for i in ("пик", "треф", "бубен", "червей")
             for j in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
             if i != suit]
    while True:
        try:
            yield from cards
        except:
            pass


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)


# alt
def card_deck(suit: str):
    suits = ['пик', 'треф', 'бубен', 'червей']
    face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    suits.remove(suit)
    while True:
        for suit_ in suits:
            for face_value in face_values:
                yield f'{face_value} {suit_}'
