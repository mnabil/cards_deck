import random


class Deck():
    def __init__(self):
        """Initializes a deck of cards"""
        self.cards = []  # List of cards , if the Data is too large, we can use a generator or a list of tuples with itertools.product
        for color in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(1, 14):  # 1-13 , 11 = Jack, 12 = Queen, 13 = King
                self.cards.append(Card(value, color))

    def shuffle(self):
        """Shuffles deck of cards"""
        random.shuffle(self.cards)

    def deal_one_card(self):
        """Deals one card from the deck"""
        if len(self.cards) == 0:
            raise ValueError('No cards left in the deck')
        else:
            return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ', '.join(map(str, self.cards))


class Card():
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return '%s-%s' % (self.value, self.color)
