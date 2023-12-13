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
        self.pipes = {}
        self.record_all_moves()

    def get_node_value(self, node):
        x, y = node
        return self.map[y][x]

    def find_start_node(self):
        for i, line in enumerate(self.map):
            if 'S' in line:
                self.pipes[0] = Pipe((line.index('S'),i), self.map)
                break
    
    def do_first_move(self):
        self.length = 1
        x, y = self.pipes[0].coords
        if self.map[y-1][x] in ['|', 'F', '7']:
            self.pipes[1] = Pipe((x, y-1), self.map)
        elif self.map[y+1][x] in ['|', 'L', 'J']:
            self.pipes[1] = Pipe((x, y+1), self.map)
        elif self.map[y][x+1] in ['-', '7', 'J']:
            self.pipes[1] = Pipe((x+1, y), self.map)
        elif self.map[y][x-1] in ['-', 'L', 'F']:
            self.pipes[1] = Pipe((x-1, y), self.map)
    
    def make_next_move(self, last_node, current_node):
        move_function = movements[current_node.value]
        # print('    move function', move_function)
        possible_moves = move_function(current_node.coords)
        # print('    possible moves', possible_moves)
        if possible_moves[0] == last_node.coords:
            return possible_moves[1]
        return possible_moves[0]
    
    def record_all_moves(self):
        self.find_start_node()
        self.do_first_move()
        # jcounter = 0 
        current_node = self.pipes[self.length]
        last_node = self.pipes[self.length-1]
        while True:
            temp = self.make_next_move(last_node, current_node)
            last_node = current_node
            current_node = Pipe(temp, self.map)
            # print('last node', last_node, 'current_node', current_node)
            if current_node.value == 'S':
                break
            # if current_node.value == 'J':
            #     jcounter += 1
            #     if jcounter > 3: break
            self.length += 1
            self.pipes[self.length] = current_node
    
    def get_furthest_node(self):
        return ceil(self.length/2)


pipeMap = PipeMap('../input/input_10.txt')

print(pipeMap.get_furthest_node())
