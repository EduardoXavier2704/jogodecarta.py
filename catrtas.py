import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Espadas', 'Paus', 'Copas', 'Ouros']
        values = list(range(2, 15))
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards, players):
        for i in range(num_cards):
            for player in players:
                player.draw(self.cards.pop())

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card)

def main():
    num_cards = 5
    deck = Deck()
    deck.shuffle()
    players = [Player("Player 1"), Player("Player 2")]
    deck.deal(num_cards, players)
    for player in players:
        player.show_hand()

if __name__ == "__main__":
    main()
