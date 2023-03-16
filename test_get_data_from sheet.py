import pandas as pd    

inventory = pd.read_excel('test 123.xlsx')
print(inventory.info())

print(inventory['COMMON NAME'])