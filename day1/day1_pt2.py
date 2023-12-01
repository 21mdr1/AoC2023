input = open("../input/input_1.txt","r").read().split("\n")

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
    
    nums.sort()
    sum+=(nums[0][1]*10)
    sum+=(nums[-1][1])

print(sum)