from parse import search

ideal = {
    'red': 12,
    'green': 13,
    'blue': 14,
    'total': 39,
}

def parse_input(hint):
    hand = {}
    hand['red'] = parse_hint(hint,"red")
    hand['green'] = parse_hint(hint,"green")
    hand['blue'] = parse_hint(hint,"blue")
    hand['total'] = hand['red'] + hand['blue'] + hand['green']
    return hand

def parse_hint(hint, color):
    r = search("{:d} " + color, hint)
    if r is None: 
        return 0
    return r[0]

def main():
    f = open("../input/input_2.txt", "r")

    game_num=0
    sum = 0

    for game in f:
        game_num+=1
        gameIsPossible = True

        hints = game.split(": ")[1].split("\n")[0].split("; ")
        for hint in hints:
            
            hand = parse_input(hint)

            if (hand['red'] > ideal['red']) or (hand['blue'] > ideal['blue']) or (hand['green'] > ideal['green']) or (hand['total'] > ideal['total']):
                gameIsPossible = False
                break
        
        if gameIsPossible: sum += game_num

    print(sum)

main()