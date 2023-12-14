
def taxicab_distance(node1, node2):
    dist = abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
    return dist

class Universe:
    def __init__(self, f):
        self.galaxies = self.record_galaxies(f)
        self.expanding_space = [[],[]] # rows, columns
        self.record_expanding_space(f)
    
    def record_galaxies(self, f):
        galaxies = [(x,y) for y in range(len(f)) for x in range(len(f[y])) 
                    if f[y][x] == '#']
        return galaxies
    
    def record_expanding_space(self, f):
        for x in range(len(f[0])):
            column = [f[y][x] for y in range(len(f))]
            if '#' not in column:
                self.expanding_space[1].append(x)
        
        for y, row in enumerate(f):
            if '#' not in row: self.expanding_space[0].append(y)
    
    def expanding_taxicab_distance(self, galaxy1, galaxy2):
        rows, columns = self.expanding_space
        x1, y1 = galaxy1; x2, y2 = galaxy2

        if y1 > y2:
            row_expansions = sum([999999 for row in rows if row in range(y2, y1)])
        else:
            row_expansions = sum([999999 for row in rows if row in range(y1, y2)])
        
        if x1 > x2:
            column_expansions = sum([999999 for column in columns if column 
                                     in range(x2, x1)])
        else:
            column_expansions = sum([999999 for column in columns if column 
                                     in range(x1, x2)])

        static_distance = taxicab_distance(galaxy1, galaxy2)
        return static_distance + row_expansions + column_expansions
    
    def sum_shortest_paths(self):
        galaxy_pairs = [(self.galaxies[i], self.galaxies[j]) 
                        for i in range(len(self.galaxies)) for j in 
                        range(i+1, len(self.galaxies))]
        
        return sum([self.expanding_taxicab_distance(*pair) for pair in 
                    galaxy_pairs])
    

f = [line.strip() for line in open('../input/input_11.txt', 'r').readlines()]

universe = Universe(f)
print(universe.sum_shortest_paths())
