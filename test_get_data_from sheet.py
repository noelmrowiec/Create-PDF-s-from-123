import sys
import pandas as pd    
def check_print_1750_column():
    inventory = pd.read_excel('test 123.xlsx')
    print(inventory.info())
    try:
        num_of_items = inventory['PRINT DD1750'].count()
        #column exists
        print("good column with count  = " +str(num_of_items))
    except KeyError:
        print("Key Error")  #todo make better
        sys.exit()
    except IndexError:
        print("Index Error")    #todo make more descriptive
        sys.exit()

check_print_1750_column()