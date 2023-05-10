from operator import index
import random
import sys
from time import process_time_ns
from tracemalloc import start
import pandas as pd    
from fillablefields import FillableFields

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

#print(new_list)

['Garmin GPS 401 S/n: 1LR061007, 1LR061007,', '1LR061007, 1LR061007,1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161, 1LR061161', 'Smae 343344535', 'ff', 'Garmin GPS 401 S/n: 1LR061007, 1LR061007,', '1LR061007, 1LR061007,1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161, 1LR061161,3 ,', '4522 , 232, 1LR061007, 1LR061007, 1LR061007,', '1LR061007,1LR061161, 1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161,', 'lass s/n: 4']


# read the excel sheet into a Pandas DataFrame
inventory_data = pd.read_excel('simple sheet test.xlsx')

# fill in blank values in the serial number column with "N/A"
inventory_data['SERIAL'].fillna('N/A', inplace=True)
items_to_print = inventory_data[inventory_data['PRINT DD-1750'] == 'x']

# group the data by name and serial number
df_combined = items_to_print.groupby(['COMMON NAME'], as_index= False).aggregate({'SERIAL' : ', '.join})
print(df_combined)

ff = FillableFields()

#box
added = True
i = 0
while added == True:
    added = ff.add_box_field(text=f"box {i}")
    i+=1

items = ff.get_box_fields()
for item in items:
    print(item)

 #contents
added = True
i = 0
while added == True:
    added = ff.add_contents_field(text=f"contents {i}")
    i+=1

items = ff.get_contents_fields()
for item in items:
    print(item)

 #init
added = True
i = 0
while added == True:
    added = ff.add_init_field(text=f"init {i}")
    i+=1

items = ff.get_init_fields()
for item in items:
    print(item)

     #spares
added = True
i = 0
while added == True:
    added = ff.add_spares_field(text=f"spares {i}")
    i+=1

items = ff.get_spares_fields()
for item in items:
    print(item)

#total
added = True
i = 0
while added == True:
    added = ff.add_total_field(text=f"total {i}")
    i+=1

items = ff.get_total_fields()
for item in items:
    print(item)

    
    #uint
added = True
i = 0
while added == True:
    added = ff.add_uint_field(text=f"uint {i}")
    i+=1

items = ff.get_uint_fields()
for item in items:
    print(item)

ff.certname = 'Noel'
print(ff.certname)