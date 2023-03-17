import sys
import pandas as pd    

def combine_same_items(inventory):
    #find all common names
    #combine serials 
    #either ouput or save
    #define how to aggregate various fields
    agg_functions = {'SERIAL': 'sum'}

    #create new DataFrame by combining rows with same id values
    #https://www.statology.org/pandas-combine-rows-with-same-column-value/
    #source https://stackoverflow.com/questions/33279940/how-to-combine-multiple-rows-of-strings-into-one-using-pandas
    #https://pandas.pydata.org/
    #df_new = inventory.groupby('COMMON NAME')
    print(inventory.info())
    # below groups items with the same common name the aggregates the serial number into one comma separted string with all of the serial number 
    df_new = inventory.groupby('COMMON NAME').aggregate({
        'SERIAL': lambda x: ', '.join([str(i) for i in x])
    })
    
    print(df_new)
    

inventory = pd.read_excel('test 123.xlsx')
def get_items_to_print_to_1750(inventory):
    # returns items from inventory that have the 'x' in the column to print the 1750
    # todo right now, must be lower case 'x'. check for both
    items_to_print = inventory[inventory['PRINT DD-1750'] == 'x']
    return items_to_print
print(get_items_to_print_to_1750(inventory)



