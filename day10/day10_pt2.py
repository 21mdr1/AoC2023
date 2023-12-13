from math import ceil

def north_to_south(currNode):
    x, y = currNode
    return (x, y+1), (x, y-1)

def east_to_west(currNode):
    x, y = currNode
    return (x+1, y), (x-1, y)

def west_to_south(currNode):
    x, y = currNode
    return (x-1, y), (x, y+1)

def east_to_south(currNode):
    x, y = currNode
    return (x, y+1), (x+1, y)

def west_to_north(currNode):
    x, y = currNode
    return (x-1, y), (x, y-1)

def east_to_north(currNode):
    x, y = currNode
    return (x+1, y), (x, y-1)

def shoelace_area(corners):
    nodes = [corner.coords for corner in corners]
    sum1 = 0
    sum2 = 0
    for i in range(len(nodes)):
        node1 = nodes[i]
        try: 
            node2 = nodes[i+1] 
        except: 
            node2 = nodes[0]
        sum1 += node1[0] * node2[1]
        sum2 += node2[0] * node1[1]
    
    return abs(sum1 - sum2) / 2

def picks_lattices(area, boundary_points):
    return int(area - boundary_points/2 + 1)

movements = {
    '|': north_to_south,
    '-': east_to_west,
    '7': west_to_south,
    'F': east_to_south,
    'J': west_to_north,
    'L': east_to_north,
}

class Pipe:
    def __init__(self, coords, map_):
        self.coords = coords
        self.value = map_[coords[1]][coords[0]]
    
    def __str__(self):
        return self.value

class PipeMap:
    def __init__(self, f):
        self.map = [list(line.strip()) for line in open(f, 'r').readlines()]
        self.length = 0
        self.corners = []
        self.record_all_moves()

    def get_node_value(self, node):
        x, y = node
        return self.map[y][x]
    
    def start_node_is_corner(self, neighbors):
        neighbor1, neighbor2 = neighbors
        if abs(neighbor1.coords[0] - neighbor2.coords[0]) == 1 and abs(neighbor1.coords[1] - neighbor2.coords[1]) == 1:
            return True
        return False

    def find_start_node(self):
        for i, line in enumerate(self.map):
            if 'S' in line:
                return Pipe((line.index('S'),i), self.map)
    
    def do_first_move(self, start):
        self.length = 1
        x, y = start.coords
        neighbors = []
        if self.map[y-1][x] in ['|', 'F', '7']:
            neighbors.append(Pipe((x, y-1), self.map))
        if self.map[y+1][x] in ['|', 'L', 'J']:
            neighbors.append(Pipe((x, y+1), self.map))
        if self.map[y][x+1] in ['-', '7', 'J']:
            neighbors.append(Pipe((x+1, y), self.map))
        if self.map[y][x-1] in ['-', 'L', 'F']:
            neighbors.append(Pipe((x-1, y), self.map))
        
        if self.start_node_is_corner(neighbors):
            self.corners.append(start)

        return neighbors[0]
    
    def make_next_move(self, last_node, current_node):
        move_function = movements[current_node.value]
        possible_moves = move_function(current_node.coords)
        if possible_moves[0] == last_node.coords:
            return possible_moves[1]
        return possible_moves[0]
    
    def record_all_moves(self):
        last_node = self.find_start_node()
        current_node = self.do_first_move(last_node)
        while True:
            if current_node.value not in ['|', '-', 'S']:
                self.corners.append(current_node)
            temp = self.make_next_move(last_node, current_node)
            last_node = current_node
            current_node = Pipe(temp, self.map)
            if current_node.value == 'S':
                break
            self.length += 1
    
    def get_furthest_node(self):
        return ceil(self.length/2)
    
    def get_inside_spaces(self):
        area = shoelace_area(self.corners)
        return picks_lattices(area, self.length+1)

pipeMap = PipeMap('../input/input_10.txt')

# print(pipeMap.get_furthest_node())
print(pipeMap.get_inside_spaces())
