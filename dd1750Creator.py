'''
1750 Creator
author: Noel Mrowiec

Creates DD-1750 PDF (packing list) from 123 excel sheet (electronic inventory spredsheet). 
Requirements: place the included DD-1750 PDF in the same folder as program because it is unprotected 
and specific field names are use by the program to fillout the PDF. Additionally, the 123 excel 
spreadsheet must have the following fields exactly as shown: 'COMMON NAME' and 'SERIAL' for the items 
and 'PRINT TO DD-1750'. The program will add the information from the excel sheet if the is a 'x' in 
the 'PRINT TO DD-1750' column. The name as serial number of the selected items (items with the 'x') 
will be added to the DD-1750 PDF. Additionally, if there are repeated items, meaning items with the 
same common name, they will be combined on the PDF and the total number of that item will be shown in 
the total's column. 
Current version limitations:
-Only use the 'simple sheet test.xlsx' because it includes the proper formating and the coulmn 
to select a print. 
-Currently, only placing the item name in the correct box with the item's serial numbers and total 
count of each item functions as expected. 
-The user cannot name the output file. Currently, it is given the name DD-Form-1750-Packing-List filled.pdf
 and the source PDF filled-out.pdf must be in the same file as the program. 

More features to follow. 
'''


from asyncio.windows_events import NULL
from csv import excel_tab
import sys
from pypdf import PdfReader, PdfWriter      
import pandas as pd                         #for read excel sheets
import re                                   #import for regex for file name checks


def contains_invalid_chars(s):
    ''' returns: True if 's' contains invalid chars for Windows filename 
    otherwise, False
    '''
    # Chars invalid for Windows file names
    invalid_chars = r"[<>\\:\"/|?*]+"
    # Check if the string contains any of the invalid characters
    return bool(re.search(invalid_chars, s))


def is_valid_filename():
    #todo not currently used because of testing
    #returns True if valid filename, otherwise false. 
    #Prompts user for a output PDF file name
    filename = input("Enter desired file name for output PDF: ")
    if contains_invalid_chars(filename):
        return False
    else:
        return True


def get_inventory():
    ''' returns: a DataFrame object (from the pandas library) containing the information from the first page.
    Prompts user to enter file name of 123 excel sheet. Waits until valid file name entered.
    '''
    #todo use is valid filename function
    while True:
        sheet_filename = input("Enter file name of valid excel sheet (must be a \"123 Sheet\"): ")
        try:
            #inventory = pd.read_excel(sheet_filename, dtype='string') # source: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-data-types
            inventory = pd.read_excel('simple sheet test.xlsx', dtype='string')    #todo remove
            return inventory
        except:
            print('You entered "' + str(sheet_filename) + '", file name not found. Check file name.')
            continue
        else:
            break       #found valid excel sheet

# todo probably remove
def num_items_to_print_1750(inventory):
    ''' Gets total number of items before combining. 
    Currently, no use for function. 
    ''' 
    try:
        num_of_items = inventory['PRINT DD-1750'].count()
        return num_of_items
    except KeyError:
        print("Key Error")  #todo make better
        sys.exit()
    except IndexError:
        print("Index Error")    #todo make more descriptive
        sys.exit()  


def get_items_to_print_to_1750(inventory):
    ''' returns: items to print to 1750 (that is, items with  a 'x' is the column)
     items from inventory that have the 'x' in the column to print the 1750
    '''
    # todo right now, must be lower case 'x'. check for both
    items_to_print = inventory[inventory['PRINT DD-1750'] == 'x']
    return items_to_print


def combine_same_items(inventory):
    ''' returns: a DataFrame object with items combined 
    todo: inventory must be a text based sheet. It doesn't work for a modified sheet for some reason.'
    '''
    #create new DataFrame by combining rows with same id values
    #https://www.statology.org/pandas-combine-rows-with-same-column-value/
    #source https://stackoverflow.com/questions/33279940/how-to-combine-multiple-rows-of-strings-into-one-using-pandas
    #https://pandas.pydata.org/
    #https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby

    #df_new = inventory.groupby('COMMON NAME')
    # groups items with the same common name and aggregates the serial number into one comma-separted string with all of the serial numbers
    
    print(inventory) #todo remove
    df_combined = inventory.groupby(['COMMON NAME'], as_index= False).aggregate({'SERIAL' : ', '.join})
    
    return df_combined


#todo check if there is no serial number 
def format_for_1750(items):
    ''' returns  a list with items formated for DD-1750

    '  items' : must be already combined DataFrame object
    '''
    list_dd1750 = list()
    for index, row in items.iterrows():
        list_dd1750.append(str(row['COMMON NAME']) + ' S/n: ' + str(row['SERIAL']))
    return list_dd1750


def char_limit_items(items_list):
    ''' returns: a list of items limited to MAX_CHARS characters per item.

    items: must a list of strings
    '''
    new_list = []

    for item in items_list:
        MAX_CHARS = 120      #todo maybe move? maybe more
        substring = item      
        split_index = 0

        while len(substring) > MAX_CHARS:
            #todo -1 means it is not found. account for this 
            split_index = substring.rindex(',', 0, MAX_CHARS) + 1     #add 1 to split after the comma
            new_list.append(substring[:split_index].strip())      
            substring = substring[split_index:]

        new_list.append(substring.strip())

    return new_list


def number_of_items(item):
    ''' returns: number of items for that object. Returns 1 if no serial numbers
    in order to get a good count, the other cells must be blank (NaN)
    Function with search a string (from the end) for 'S/n' and count all the serial numbers after it for the total count. If there is no 'S/n', the total count will be 1, otherwise the total count will be the number of serial numbers which are separted by commas. Case matters. 

    item: must be all items for that item. Should not be split over lines or will get bad result. Must be combined and formatted with 'S/n'. Example: 'Garmin GPS 401 S/n: 1LR061007, 1LR061161' will return 2
    '''
    #todo assume that all have serial number. Need to change this
    start_index = item.rfind('S/n')
    if(start_index != -1):
        #'S/n' is in the string
        start_index += 3    #start index after 'S/n'
        serial_nums = item.split(',')
        return len(serial_nums)

    return 1

'''
'''
def select_field(field_selection, num, contents, fillable_fields_dict):
    if 'box' in field_selection:
        fill_box_field(num, contents, fillable_fields_dict)
    elif 'contents' in field_selection:
        fill_contents_field(num, contents, fillable_fields_dict)
    elif 'unit' in field_selection:
        fill_unit_field(num, contents, fillable_fields_dict)
    elif 'init' in field_selection:
        fill_init_field(num, contents, fillable_fields_dict)
    elif 'spares' in field_selection:
        fill_spares_field(num, contents, fillable_fields_dict)
    elif 'total' in field_selection:
        fill_total_field(num, contents, fillable_fields_dict)


''' returns: a fillable_fields_dict with the specified field containing the contents
'''
def fill_field(field_selection, num, contents, fillable_fields_dict):
    ''' Returns: the fillable_fields_dict. 
    fills the specified dict (properly formated) with the field filled 

    field_selection: string for the field selected ex) 'total_' or 'contents_'
    num: must be int. this is the index of of the field
    contents: count of the number of items
    fillable_fields_dict: dict for the 1750 PDF
    '''
    MAX_NUM = 18    #todo maybe not all the same
    if(num <= MAX_NUM):
        field = field_selection + str(num)
        fillable_fields_dict[field] = contents

    return fillable_fields_dict
    
#print(intro) todo print 

# prompt user for input excel sheet file name
inventory = get_inventory()

# added "PRINT DD-1750 column to the sheet
    #if the column contains a 'x', print to dd-1750
    
#todo options: should have a deployable, or something like that, column for items to add to 1750
#   but could ask user to enter in the sheet name to search, also the column number or names to add data to sheet

# get data from excel sheet
items = get_items_to_print_to_1750(inventory)


# puts all the items with the same 'common name' on the same line with the serial numbers
items_combined = combine_same_items(items)

items = format_for_1750(items_combined)

items = char_limit_items(items)

#for each item in items 
#add to contents field while there is space
#todo make new page if not space
#add the data to the dict below which will print to the DD-1750
fillable_fields_dict = {'box_1': '', 'contents_1': '', 'unit_1': '', 'init_1': '', 'box_2': '', 'contents_2': '', 'unit_2': '', 'init_2': '', 'spares_2': '', 'box_3': '', 'contents_3': '', 'unit_3': '', 'init_3': '', 'spares_3': '', 'box_4': '', 'contents_4': '', 'unit_4': '', 'init_4': '', 'spares_4': '', 'box_5': '', 'contents_5': '', 'unit_5': '', 'init_5': '', 'spares_5': '', 'contents_6': '', 'unit_6': '', 'init_6': '', 'spares_6': '', 'box_6': '', 'init_7': '', 'spares_7': '', 'box_7': '', 'contents_7': '', 'unit_7': '', 'box_8': '', 'contents_8': '', 'unit_8': '', 'init_8': '', 'spares_8': '', 'box_9': '', 'contents_9': '', 'unit_9': '', 'init_9': '', 'spares_9': '', 'box_10': '', 'contents_10': '', 'unit_10': '', 'init_10': '', 'spares_10': '', 'box_11': '', 'contents_11': '', 'unit_11': '', 'init_11': '', 'spares_11': '', 'box_12': '', 'contents_12': '', 'unit_12': '', 'init_12': '', 'spares_12': '', 'box_13': '', 'contents_13': '', 'unit_13': '', 'init_13': '', 'spares_13': '', 'box_14': '', 'contents_14': '', 'unit_14': '', 'init_14': '', 'spares_14': '', 'box_15': '', 'contents_15': '', 'unit_15': '', 'init_15': '', 'spares_15': '', 'box_16': '', 'contents_16': '', 'unit_16': '', 'init_16': '', 'spares_16': '', 'box_17': '', 'contents_17': '', 'unit_17': '', 'init_17': '', 'spares_17': '', 'box_18': '', 'contents_18': '', 'unit_18': '', 'init_18': '', 'spares_18': '', 'certname': '', 'end_item': '', 'packed_by': '', 'no_boxes': '', 'req_no': '', 'order_no': '', 'date': '', 'total_pages': '', 'spares_1': '', 'cur_page': '', 'total_1': '', 'total_2': '', 'total_3': '', 'total_6': '', 'total_4': '', 'total_5': '', 'total_7': '', 'total_8': '', 'total_9': '', 'total_10': '', 'total_11': '', 'total_12': '', 'total_13': '', 'total_14': '', 'total_15': '', 'total_16': '', 'total_17': '', 'total_18': ''}
    
for index, item in enumerate(items, start=1):
    count = number_of_items(item) #todo wrong count b/c split over lines. must change in future
    items = fill_field('contents_',index, item, fillable_fields_dict)
    #total item
    items = fill_field('total_',index, count, fillable_fields_dict)
#todo if not, make new page


# todo ask  to output dd1750 or da-2062
# todo translate the fields in the excel sheet to the 1750 or 2062 
# todo get correct sum the columns and put total in total_#
# todo prompt user for output filename
# todo check valid

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