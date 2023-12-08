from classes import *

f = open("../input/input_8.txt","r").read().split('\n')
map_ = Map(f)
print(map_.traverse())