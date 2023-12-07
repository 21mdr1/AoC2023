hand_types = {
    'five of a kind': 7,
    'four of a kind': 6,
    'full house': 5,
    'three of a kind': 4,
    'two pair': 3,
    'one pair': 2,
    'high card': 1
}

class Game:
    def __init__(self, f):
        self.hands = []
        self.initialize(f)
    
    def initialize(self, f):
        for hand in f.split('\n'):
            cards, bet = hand.split()
            self.hands.append(Hand(cards, int(bet)))
        self.sort_hands()
    
    def sort_hands(self):
        self.hands.sort()

    def calculate_total_winnings(self):
        winnings = [(i+1)*hand.bet for i, hand in enumerate(self.hands)]
        return sum(winnings)

class Hand:
    def __init__(self, cards, bet):
        self.cards = []
        self.bet = bet
        self.hand_type = ''
        self.initialize(cards)

    def initialize(self, cards):
        for card in cards:
            self.cards.append(Card(card))
        
        self.hand_type = self.determine_hand_type()

    def determine_hand_type(self):
        sorted_cards = sorted(self.cards)

        if sorted_cards[0] == sorted_cards [4]:
            return hand_types['five of a kind']
        
        if sorted_cards[0] == sorted_cards[3] or sorted_cards[1] == sorted_cards[4]:
            return hand_types['four of a kind']
        
        if sorted_cards[0] == sorted_cards[2]:
            if sorted_cards[3] == sorted_cards[4]: 
                return hand_types['full house']
            else: return hand_types['three of a kind']
        if sorted_cards[1] == sorted_cards[3]:
            return hand_types['three of a kind']
        if sorted_cards[2] == sorted_cards[4]:
            if sorted_cards[0] == sorted_cards[1]:
                return hand_types['full house']
            else: return hand_types['three of a kind']
        
        if sorted_cards[0] == sorted_cards[1]:
            if sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4]:
                return hand_types['two pair']
            else: return hand_types['one pair']
        if sorted_cards[1] == sorted_cards[2]:
            if sorted_cards[3] == sorted_cards[4]:
                return hand_types['two pair']
            else: return hand_types['one pair']
        if sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4]:
            return hand_types['one pair']
        
        return hand_types['high card']
    
    def __str__(self):
        string = ''
        for card in self.cards: string += str(card)
        return string + ' ' + str(self.bet)

    
    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.cards[i] < other.cards[i]
            return False # if we get here, they're the same hand
        return self.hand_type < other.hand_type

    
class Card:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        court_cards = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
        }
        our_value = int(self.value) if self.value.isdigit() else court_cards[self.value]
        their_value = int(other.value) if other.value.isdigit() else court_cards[other.value]
        return our_value < their_value
    
    def __str__(self):
        return self.value
        

f = open("../input/input_7.txt", "r").read()
game = Game(f)

print(game.calculate_total_winnings())