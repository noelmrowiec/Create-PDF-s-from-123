from operator import index
import random
import sys
from time import process_time_ns
from tracemalloc import start
import pandas as pd    

items = ['aaaaaaaaaaaa', 'ffffffffffffff', 'ggggggggggggggg','hhh', 'garmin 234, 234234234, 234255235253535, 55555555555555555555555555555555555555555555555, 4444, 45334, 2232323, 4333','kkkkkkkkk' ]



s = 'Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007,\
1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161'
s2 = 'Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007,\
1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161,3 ,4522 , 232, 1LR061007, 1LR061007, 1LR061007, 1LR061007,\
1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161,'
items_list = [s, 'Smae 343344535', 'ff', s2, 'lass s/n: 4']

new_list = []

for item in items_list:
    MAX_CHARS = 50
    substring = item      
    split_index = 0

    while len(substring) > MAX_CHARS:
        split_index = substring.rfind(',', 0, MAX_CHARS) + 1     #add 1 to split after the comma
        new_list.append(substring[:split_index].strip())      
        substring = substring[split_index:]

    new_list.append(substring.strip())

print(new_list)

['Garmin GPS 401 S/n: 1LR061007, 1LR061007,', '1LR061007, 1LR061007,1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161, 1LR061161', 'Smae 343344535', 'ff', 'Garmin GPS 401 S/n: 1LR061007, 1LR061007,', '1LR061007, 1LR061007,1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161, 1LR061161,3 ,', '4522 , 232, 1LR061007, 1LR061007, 1LR061007,', '1LR061007,1LR061161, 1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161,', 'lass s/n: 4']