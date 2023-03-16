import sys
import pandas as pd    

def get_items_to_print_to_1750(inventory):
    # returns items from inventory that have the 'x' or 'X' in the column to print the 1750
    items_to_print = inventory[inventory['PRINT DD-1750'] == 'x']
    print(items_to_print)


inventory = pd.read_excel('test 123.xlsx')
get_items_to_print_to_1750(inventory)


