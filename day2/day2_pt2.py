from parse_input import parse_input

def main():
    f = open("../input/input_2.txt", "r")

    sum = 0

    for game in f:
        red = 0
        green = 0
        blue = 0

        hints = game.split(": ")[1].split("\n")[0].split("; ")
        for hint in hints:
            
            hand = parse_input(hint)
            if hand['red'] > red:
                red = hand['red']
            if hand['green'] > green:
                green = hand['green']
            if hand['blue'] > blue: 
                blue = hand['blue']
        
        sum += (red*green*blue)

    print(sum)

main()