
from parse import parse

class Node:
    def __init__(self, value, left, right):
        # self.map = Map
        self.value = value
        self.right = right
        self.left = left

class Map:
    def __init__(self, f):
        self.nodes = {}
        self.directions = f[0]
        self.initialize(f[2:])
    
    def initialize(self, nodes):
        for node in nodes:
            value, left, right = parse("{} = ({}, {})", node)
            self.nodes[value] = Node(value, left, right)

    def go_left(self, node):
        return self.nodes[node.left] 
    
    def go_right(self, node):
        return self.nodes[node.right]
    
    def traverse(self):
        current_node = self.nodes['AAA']
        steps = 0
        i = 0

        while True:
            if current_node.value == 'ZZZ':
                return steps
            direction = self.directions[i]
            if direction == 'R':
                current_node = self.go_right(current_node)
            else: 
                current_node = self.go_left(current_node)

            steps += 1
            i += 1
            if i >= len(self.directions): i = 0
            
            

    
f = open("../input/input_8.txt","r").read().split('\n')
map_ = Map(f)
print(map_.traverse())
