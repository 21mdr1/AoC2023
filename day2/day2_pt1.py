from parse_input import parse_input

ideal = {
    'red': 12,
    'green': 13,
    'blue': 14,
    'total': 39,
}

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