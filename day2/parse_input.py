from parse import search

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
