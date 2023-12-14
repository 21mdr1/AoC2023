import re
import itertools

def possibilities(template):
    # template: ???.### 
    unknown_num = len(re.findall('\?', template))
    missing = map(list, itertools.product('.#', repeat=unknown_num))

    possibilities = [
        ''.join([i if i != '?' else permutation.pop(0) for i in template]) 
        for permutation in missing
    ]
    return possibilities

def regex(template):
    # template: 1,1,3
    template = template.split(',')
    regex = '\.*' + '\.+'.join(['#{' + num + '}' for num in template]) + '\.*'
    return regex

def number_of_matches(template1, template2):
    return sum([1 if re.fullmatch(regex(template2), possibility) is not None 
               else 0 for possibility in possibilities(template1)])

def solve_springs(f):
    return sum([number_of_matches(line[0], line[1]) for line in f])

def records(f):
    return [line.strip().split(' ') for line in open(f, 'r').readlines()]

print(solve_springs(records('../input/input_12.txt')))