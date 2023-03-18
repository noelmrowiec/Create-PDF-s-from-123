from operator import index
import sys
import pandas as pd    

line = ['aaaaaaaaaaaa', 'ffffffffffffff', 'ggggggggggggggg','hhh', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj','kkkkkkkkk' ]
n = 12
newList=  []
for element in line:
    if len(element)> 12:
        """Produce `n`-character chunks from `s`."""
        for start in range(0, len(element), n):
            newList.append(element[start:start+n])
    else:
        newList.append(element)
print(newList)
