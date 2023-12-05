from math import floor
from parse import parse

class Game:
    def __init__(self, f):
        self.cards = [line.split("\n")[0] for line in f.readlines()]
        self.card_copies = [1]*len(self.cards)

    def play(self):
        for i in range(len(self.cards)):
            card = Card(self.cards[i])

            for j in range(1, card.score+1):
                try: self.card_copies[i+j]+=self.card_copies[i]
                except: break
    
        return sum(self.card_copies)
            

class Card:
    def __init__(self, card_info):
        self.winning, self.yours = self.split_numbers(card_info)
        self.score = self.score_card()
    
    def split_numbers(self, card_info):
        _, winning, yours = parse("Card {}: {} | {}", card_info)
        return [i for i in winning.split(" ") if not i == '' ], [j for j in yours.split(" ") if not j == '']

    def score_card(self):
        return len([number for number in self.yours if number in self.winning])
        

game = Game(open("../input/input_4.txt","r"))
print(game.play())

