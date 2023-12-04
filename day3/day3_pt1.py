from re import finditer

f = open("../input/input_3.txt", "r").readlines()

class Engine:
    def __init__(self, f):
        self.iter = f
        self.symbols = [] #(x,y)
        self.get_symbols() 
    
    def get_symbols(self):
        counter = -1
        for line in f:
            counter+=1
            line = line.split("\n")[0]
            for match in finditer(r'[^0-9.]', line): #finds symbols
                self.symbols.append((counter,match.start()))

    def check_part(self, part):
        for neighbor in part.neighbors: 
            if neighbor in self.symbols:
                part.isPart = True
                break
        return part.isPart

    def get_parts(self):
        sum = 0
        counter = -1
        for line in self.iter:
            counter+=1
            line = line.split("\n")[0]
            for match in finditer(r'\d+', line):
                part = Part(counter, match.start(), match.end(), match.group())
                if self.check_part(part): sum+=part.value

        return sum

class Part:
    def __init__(self, line, start, end, value):
        self.isPart = False
        self.value = int(value)
        self.neighbors = self.get_neighbors(line, start, end)
    
    def get_neighbors(self, line, start, end):
        return [(x,y) for x in range(line-1, line+2) for y in range(start-1, end+1)]


engine = Engine(f)
print(engine.get_parts())

