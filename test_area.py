from operator import index
import random
import sys
from time import process_time_ns
import pandas as pd    

items_or = ['aaaaaaaaaaaa', 'ffffffffffffff', 'ggggggggggggggg','hhh', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj','kkkkkkkkk' ]

items = []
for i in range (1000000):
    items.append('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
n = 12
newList=  []
start_a = process_time_ns()
for line in items:

    if len(line)> 12:
        """Produce `n`-character chunks from `line`."""
        for i in range(0, len(line), n):
            newList.append(line[i:i+n])
    else:
        newList.append(line)
stop_a = process_time_ns()
print('time a')
print(stop_a - start_a)

newListb=  []
start_b = process_time_ns()

stop_b = process_time_ns()
print('time b')
print(stop_b - start_b)