from re import finditer

f = [line.split("\n")[0] for line in open("../input/input_3.txt", "r").readlines()] 

class Engine:
    def __init__(self, f):
        self.map = f
        self.parts = self.get_parts()
        self.gears = self.get_gears()
    
    def get_parts(self):
        parts = []
        counter = -1
        for line in self.map:
            counter+=1
            for match in finditer(r'\d+', line):
                parts.append(Part(counter, match.start(), match.end(), match.group()))
        return parts

    def get_gears(self):
        gears = []
        counter = -1
        for line in self.map:
            counter+=1
            for match in finditer(r'[*]', line):
                gears.append(Gear(counter, match.start()))
        return gears
    
    def attach_parts(self):
        for gear in self.gears:
            for part in self.parts:
                match = [coord for coord in part.coords if coord in gear.neighbors]
                if len(match) > 0:
                    gear.parts.append(part)
    
    def calculate_gear_ratio(self):
        self.attach_parts()
        return sum([gear.ratio() for gear in self.gears])


class Gear:
    def __init__(self, line, position):
        self.coords = (line, position)
        self.neighbors = [(x, y) for x in range(line-1, line+2) for y in range(position-1, position+2) if not (x == line and y == position)]
        self.parts = []

    def ratio(self):
        if len(self.parts) == 2:
            return self.parts[0].value * self.parts[1].value
        return 0

class Part:
    def __init__(self, line, start, end, value):
        self.value = int(value)
        self.coords = self.get_coords(line, start, end)

    def get_coords(self, line, start, end):
        return [(line, x) for x in range(start, end)]

    



engine = Engine(f)
print(engine.calculate_gear_ratio())

# counter = -1
# for line in engine.map:
#     counter+=1
#     for match in finditer(r'\d+', line):
#         Part(counter, match.start(), match.end(), match.group())