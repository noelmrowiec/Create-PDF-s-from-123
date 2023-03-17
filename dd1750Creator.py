from asyncio.windows_events import NULL
from csv import excel_tab
import sys
from pypdf import PdfReader, PdfWriter      
import pandas as pd                         #for read excel sheets
import re                                   #import for regex for file name checks

def contains_invalid_chars(s):
    # Chars invalid for Windows file names
    invalid_chars = r"[<>\\:\"/|?*]+"
    # Check if the string contains any of the invalid characters
    return bool(re.search(invalid_chars, s))


def is_valid_filename():
    #returns todo
    #Prompts user for a output PDF file name 
    filename = input("Enter desired file name for output PDF: ")
    if contains_invalid_chars(filename):
        return False
    else:
        return True

''' returns: a DataFrame object (from the pandas library) containing the information from the first page.
Prompts user to enter file name of 123 excel sheet. Waits until valid file name entered.
'''
def get_inventory():
    while True:
        sheet_filename = input("Enter file name of valid excel sheet (must be a \"123 Sheet\"): ")
        try:
            inventory = pd.read_excel('simple sheet test.xlsx', dtype='string') #todo change back to sheet_filename # source: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-data-types
            return inventory
        except:
            print('You entered "' + str(sheet_filename) + '", file name not found. Check file name.')
            continue
        else:
            break       #found valid excel sheet


def num_items_to_print_1750(inventory):
    try:
        num_of_items = inventory['PRINT DD-1750'].count()
        return num_of_items
    except KeyError:
        print("Key Error")  #todo make better
        sys.exit()
    except IndexError:
        print("Index Error")    #todo make more descriptive
        sys.exit()  

''' returns: items to print to 1750 (that is, items with  a 'x' is the column)
'''
def get_items_to_print_to_1750(inventory):
    # returns items from inventory that have the 'x' in the column to print the 1750
    # todo right now, must be lower case 'x'. check for both
    items_to_print = inventory[inventory['PRINT DD-1750'] == 'x']
    return items_to_print

''' returns: a DataFrame object with items combined 
'''
def combine_same_items(inventory):
    #find all common names
    #combine serials 
    #either ouput or save
    #define how to aggregate various fields

    #create new DataFrame by combining rows with same id values
    #https://www.statology.org/pandas-combine-rows-with-same-column-value/
    #source https://stackoverflow.com/questions/33279940/how-to-combine-multiple-rows-of-strings-into-one-using-pandas
    #https://pandas.pydata.org/
    #https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby

    #df_new = inventory.groupby('COMMON NAME')
    # groups items with the same common name and aggregates the serial number into one comma-separted string with all of the serial numbers

    df_combined = inventory.groupby(['COMMON NAME'], as_index= False).aggregate({'SERIAL' : ', '.join})
    
    return df_combined
        
# prompt user for input excel sheet file name
inventory = get_inventory()
# excel sheet doesn't work with default 123. Must create a new one
# added "PRINT DD-1750 column to the sheet
    #if the column contains a 'x', print to dd-1750
    #in order to get a good count, the other cells must be blank (NaN)

#options: should have a deployable, or something like that, column for items to add to 1750
#   but could ask user to enter in the sheet name to search, also the column number or names to add data to sheet

# get data from excel sheet
items = get_items_to_print_to_1750(inventory)


# should put all the items with the same 'common name' on the same line with the serial numbers

# must check that it fits on one spot

#add the data to the dict below which will print to the DD-1750
fillable_fields_dict = {'box_1': '', 'contents_1': '', 'unit_1': '', 'init_1': '', 'box_2': '', 'contents_2': '', 'unit_2': '', 'init_2': '', 'spares_2': '', 'box_3': '', 'contents_3': '', 'unit_3': '', 'init_3': '', 'spares_3': '', 'box_4': '', 'contents_4': '', 'unit_4': '', 'init_4': '', 'spares_4': '', 'box_5': '', 'contents_5': '', 'unit_5': '', 'init_5': '', 'spares_5': '', 'contents_6': '', 'unit_6': '', 'init_6': '', 'spares_6': '', 'box_6': '', 'init_7': '', 'spares_7': '', 'box_7': '', 'contents_7': '', 'unit_7': '', 'box_8': '', 'contents_8': '', 'unit_8': '', 'init_8': '', 'spares_8': '', 'box_9': '', 'contents_9': '', 'unit_9': '', 'init_9': '', 'spares_9': '', 'box_10': '', 'contents_10': '', 'unit_10': '', 'init_10': '', 'spares_10': '', 'box_11': '', 'contents_11': '', 'unit_11': '', 'init_11': '', 'spares_11': '', 'box_12': '', 'contents_12': '', 'unit_12': '', 'init_12': '', 'spares_12': '', 'box_13': '', 'contents_13': '', 'unit_13': '', 'init_13': '', 'spares_13': '', 'box_14': '', 'contents_14': '', 'unit_14': '', 'init_14': '', 'spares_14': '', 'box_15': '', 'contents_15': '', 'unit_15': '', 'init_15': '', 'spares_15': '', 'box_16': '', 'contents_16': '', 'unit_16': '', 'init_16': '', 'spares_16': '', 'box_17': '', 'contents_17': '', 'unit_17': '', 'init_17': '', 'spares_17': '', 'box_18': '', 'contents_18': '', 'unit_18': '', 'init_18': '', 'spares_18': '', 'certname': '', 'end_item': '', 'packed_by': '', 'no_boxes': '', 'req_no': '', 'order_no': '', 'date': '', 'total_pages': '', 'spares_1': '', 'cur_page': '', 'total_1': '', 'total_2': '', 'total_3': '', 'total_6': '', 'total_4': '', 'total_5': '', 'total_7': '', 'total_8': '', 'total_9': '', 'total_10': '', 'total_11': '', 'total_12': '', 'total_13': '', 'total_14': '', 'total_15': '', 'total_16': '', 'total_17': '', 'total_18': ''}
    


# ask  to output dd1750 or da-2062
# translate the fields in the excel sheet to the 1750 or 2062 
# sum the columns and put total in total_#
# prompt user for output filename
# check valid
# save as new PDF

# below from https://pypdf.readthedocs.io/
reader = PdfReader("DD-Form-1750-Packing-List different version.pdf")
writer = PdfWriter()


#print(reader.get_form_text_fields(True))


page = reader.pages[0]   # from https://pypdf.readthedocs.io/
fields = reader.get_fields()     # from https://pypdf.readthedocs.io/





writer.add_page(page)   # from https://pypdf.readthedocs.io/
writer.update_page_form_field_values(writer.pages[0], fillable_fields_dict) # from https://pypdf.readthedocs.io/



# write "output" to pypdf-output.pdf # below from https://pypdf.readthedocs.io/
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)