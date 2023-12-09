from parse import parse
from math import lcm

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

class Map:
    def __init__(self, f):
        self.nodes = {}
        self.directions = f[0]
        self.start_nodes = []
        self.initialize(f[2:])
    
    def initialize(self, nodes):
        for node in nodes:
            value, left, right = parse("{} = ({}, {})", node)
            self.nodes[value] = Node(value, left, right)
            if value.endswith('A'): self.start_nodes.append(value)

    def go_left(self, node):
        return self.nodes[node.left] 
    
    def go_right(self, node):
        return self.nodes[node.right]

    def follow_path(self, start_node):
        current_node = self.nodes[start_node]
        steps = 0
        i = 0

        while True:
            if current_node.value.endswith('Z'):
                return steps
            direction = self.directions[i]
            if direction == 'R':
                current_node = self.go_right(current_node)
            else: 
                current_node = self.go_left(current_node)

            steps += 1
            i += 1
            if i >= len(self.directions): i = 0

    def traverse(self):
        paths = [paths.append(self.follow_path(node)) for node in self.start_nodes]

        return lcm(*paths)
