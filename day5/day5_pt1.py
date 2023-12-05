
def mapping(input, rules):
    for rule in rules:
        destination, source, rng = rule
        if input in range(source, source + rng):
            diff = input - source
            return destination + diff
    return input

class Almanac:
    def __init__(self, f):
        self.conversions = []
        self.seeds = []
        self.rulesets = {}
        self.initialize(f)
    
    def initialize(self, f):
        self.parse_seeds(f[0])

        for i in range(1, len(f)):
            self.parse_rules(f[i])
    
    def parse_seeds(self, seeds):
        temp = seeds.split(': ')[1].split(' ')
        self.seeds = list(map(int, temp))
    
    def parse_rules(self, ruleset):
        conversion = ruleset.split("\n")[0]
        temp = ruleset.split("\n")[1:]
        self.conversions.append(conversion)
        self.rulesets[conversion] = [list(map(int, line.split(' '))) for line in temp]

    def get_soil_numbers(self):
        soil_nums = self.seeds
        for conversion in self.conversions:
            soil_nums = [mapping(num, self.rulesets[conversion]) for num in soil_nums]
        
        return soil_nums

file = open("../input/input_5.txt", "r").read().split("\n\n") 
soil = Almanac(file).get_soil_numbers()

print(min(soil))