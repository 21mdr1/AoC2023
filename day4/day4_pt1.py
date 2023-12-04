from math import floor
from parse import parse

class Game:
    def __init__(self, line):
        self.winning, self.yours = self.split_numbers(line)
        self.score = self.score_game()
    
    def split_numbers(self, line):
        _, winning, yours = parse("Card {}: {} | {}", line.split("\n")[0])
        return [i for i in winning.split(" ") if not i == '' ], [j for j in yours.split(" ") if not j == '']

    def score_game(self):
        matches = 0
        for number in self.yours:
            if number in self.winning: matches+=1;
        return floor(2**(matches-1))
        

sum = 0
for line in open("../input/input_4.txt","r"):
    game = Game(line)
    sum += game.score

print(sum)
