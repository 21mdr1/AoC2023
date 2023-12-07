# input = open("../input/input_1.txt","r").read().split("\n")
input = open("../input/test/test_input_1_2.txt","r").read().split("\n")

numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def naive(input):
    sum = 0
    for line in input:

        # (index, num)
        nums = []

        for i in range(len(line)):
            #digit
            if line[i].isdigit(): nums.append((i, int(line[i]))); continue
            #written
            for j in range(3,7):
                if line[i:i+j]in numbers: nums.append((i,numbers[line[i:i+j]])); break
        
        sum+=(nums[0][1]*10)
        sum+=(nums[-1][1])

    print(sum)

# naive(input)

# Using regex:
from re import search

def regex(input):
    sum = 0
    
    for line in input:
        first = search(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line).group(0)
        last = search(r'\d|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1]).group(0)

        try: 
            first = int(first)
        except:
            first = numbers[first]

        try: 
            last = int(last)
        except:
            last = numbers[last[::-1]]

        sum+=(first*10 + last)
       
    print(sum)

regex(input)