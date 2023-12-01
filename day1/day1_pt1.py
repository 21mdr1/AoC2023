input = open("../input/input_1.txt","r").read().split("\n")

sum = 0

for line in input:
    # Find first num
    for char in line:
        if char.isdigit(): sum += int(char)*10; break
    # Find last num
    for char in reversed(line):
        if char.isdigit(): sum += int(char); break

print(sum)