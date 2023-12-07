
def mapping(num, rule):
    if rule == None:
        return num
    destination, source, rng = rule
    diff = num - source
    return destination + diff

def checking(seed_range, rules, implicit_rules):
    start, end = seed_range
    start_rule = end_rule = None
    dest_ranges = []

    # get what rules start and end fall under
    for rule in rules:
        _, source, rng = rule
        if start in range(source, source + rng):
            start_rule = rule
        if end in range(source, source + rng):
            end_rule = rule
    
    # get rulesets for when start or end fall in an implicit ruleset
    for rule in implicit_rules:
        _, source, rng = rule
        if start_rule == None and (start >= source and start <= source + rng + 1):
            start_rule = rule
        if end_rule == None and (end >= source and end <= source + rng + 1):
            end_rule = rule 

    # check if they fall under the same rule
    if start_rule == end_rule:
        dest_ranges.append((mapping(start, start_rule), mapping(end, end_rule)))
        return dest_ranges
    
    # if they don't, check if the two ranges make up seed_range
    _, source, rng = start_rule
    start_rule_top = source + rng - 1

    _, source, rng = end_rule
    end_rule_bottom = source

    dest_ranges.append((mapping(start, start_rule), mapping(start_rule_top, start_rule)))
    dest_ranges.append((mapping(end_rule_bottom, end_rule), mapping(end, end_rule)))

    if start_rule_top + 1 == end_rule_bottom:
        return dest_ranges

    # if they don't, call this function on the middle range
    dest_ranges += checking((start_rule_top + 1, end_rule_bottom - 1), rules, implicit_rules)

    return dest_ranges

class Almanac:
    def __init__(self, f):
        self.conversions = []
        self.seed_ranges = []
        self.rulesets = {}
        self.implicit_rules = {}
        self.initialize(f)
    
    def initialize(self, f):
        self.parse_seeds(f[0])

        for i in range(1, len(f)):
            self.parse_rules(f[i])

        for key in self.rulesets:
            self.get_implicit_rules(key, self.rulesets[key])
    
    def parse_seeds(self, seeds):
        temp = [int(seed) for seed in seeds.split(': ')[1].split(' ')]
        for i in range(0, len(temp), 2):
            self.seed_ranges.append((temp[i], temp[i] + temp[i+1] + 1))
    
    def parse_rules(self, ruleset):
        conversion = ruleset.split("\n")[0]
        temp = ruleset.split("\n")[1:]
        self.conversions.append(conversion)
        self.rulesets[conversion] = [list(map(int, line.split(' '))) for line in temp]

    def get_implicit_rules(self, conversion, ruleset):
        implicit_rules = []
        ruleset = sorted(ruleset, key=lambda x: x[1])
        for i, rule in enumerate(ruleset):
            if i == 0 and rule[1] > 1:
                implicit_rules.append([1, 1, rule[1]-1])
            if i == len(ruleset) - 1:
                implicit_rules.append([rule[1] + rule[2], rule[1] + rule[2], float('inf')])
                continue
            start = ruleset[i-1][1] + ruleset[i-1][2]
            rng = rule[1] - start
            implicit_rules.append([start, start, rng])
        self.implicit_rules[conversion] = implicit_rules

    def get_min_soil_number(self):
        dest_ranges = self.seed_ranges

        for conversion in self.conversions:
            temp = []
            for rnge in dest_ranges:
                temp += checking(rnge, self.rulesets[conversion], self.implicit_rules[conversion])
            dest_ranges = temp
        
        min_range = min(dest_ranges)
        return min_range[0]

file = open("../input/input_5.txt", "r").read().split("\n\n") 
soil = Almanac(file).get_min_soil_number()

print(soil)