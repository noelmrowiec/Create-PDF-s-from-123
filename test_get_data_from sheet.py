import sys
import pandas as pd    

def something(inventory):
    #find all common names
    #combine serials 
    #either ouput or save
    #define how to aggregate various fields
    agg_functions = {'SERIAL': 'sum'}

    #create new DataFrame by combining rows with same id values
    #https://www.statology.org/pandas-combine-rows-with-same-column-value/
    #df_new = inventory.groupby('COMMON NAME')
    print(inventory.info())
    df_new = inventory.groupby('COMMON NAME').aggregate({'SERIAL': lambda x: ', '.join(str(x))})
    
    print(df_new)

    df = pd.DataFrame({
    'category': ['A'] * 2 + ['B'] * 2,
    'name': [3331.0, '22', 'A3', 'B144'],
    })

    #df2 = df.groupby('category').agg({
    #    'name': lambda x: ', '.join(str(x)),
    #})
    #print(df2)

    
    df2 = df.groupby('category').agg({
        'name': lambda x: ', '.join([str(i) for i in x]),
    })
    print(df2)

    ## Create a dictionary to store the mapping functions for each category
    #name_mapping = {'A': lambda x: ' '.join([str(i) for i in x]), 'B': lambda x: ' '.join([str(i) for i in x])}

    ## Group the DataFrame by 'category' and apply the corresponding mapping function to each group
    #df['name'] = df.groupby('category')['name'].apply(lambda x: name_mapping[x.name](x.tolist()))

    #print(df)
    

inventory = pd.read_excel('test 123.xlsx')
something(inventory)


