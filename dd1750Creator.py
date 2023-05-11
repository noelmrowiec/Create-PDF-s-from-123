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

- 18APR: Note: Common name cannot be blank, otherwise it will not be added to list  
'''

import logging
import sys
logging.basicConfig(filename='dd1750CreatorLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
try:
    from fillablefields import FillableFields
    from pypdf import PdfReader, PdfWriter      
    import pandas as pd                #for read excel sheets
    import re                          #import for regex for file name checks
except:
    logging.critical("Library imports failed")
    print("Unable to import 3rd party libraries. Check that pypdf and pandas and installed.")
    sys.exit()


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
            inventory = pd.read_excel(sheet_filename, dtype='string')    
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
    
    #for i, v in enumerate(inventory['PRINT DD-1750']):
    #    #convert all 'x' to lowercase
    #    if v == 'x' or v == 'X':
            
    #        inventory['PRINT DD-1750'][i] = v.lower()
    #        print(inventory['PRINT DD-1750'][i])
    
    items_to_print = inventory[inventory['PRINT DD-1750'] == 'x']
    return items_to_print


def combine_same_items(inventory):
    ''' returns: a DataFrame object with items combined 
    todo: inventory must be a text based sheet. It doesn't work for a modified sheet for some reason.'
    Precondition: COMMON NAME must not be blank otherwise this function will not include it
    '''
    #create new DataFrame by combining rows with same id values
    #https://www.statology.org/pandas-combine-rows-with-same-column-value/
    #source https://stackoverflow.com/questions/33279940/how-to-combine-multiple-rows-of-strings-into-one-using-pandas
    #https://pandas.pydata.org/
    #https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby

    #df_new = inventory.groupby('COMMON NAME')
    # groups items with the same common name and aggregates the serial number into one comma-separted string with all of the serial numbers
    
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

def char_limit_item(item):
    ''' returns: a list of the item split up as MAX_CHARS characters per line.

    item: must a single string with item info
    '''
    new_list = []
    MAX_CHARS = 120      #todo maybe move? maybe more
    substring = item      
    split_index = 0

    while len(substring) > MAX_CHARS:
        #todo -1 means it is not found. account for this 
        split_index = substring.rindex(',', 0, MAX_CHARS) + 1     #add 1 to split after the comma
        new_list.append(substring[:split_index].strip())      
        substring = substring[split_index:]

        #index += 1;                 # update index of split

    new_list.append(substring.strip())

    return new_list

def char_limit_items(items_list):
    ''' returns: a list of items limited to MAX_CHARS characters per item.

    items: must a list of strings
    '''
    new_list = []

    for index, item in enumerate(items_list):
        MAX_CHARS = 120      #todo maybe move? maybe more
        substring = item      
        split_index = 0

        while len(substring) > MAX_CHARS:
            #todo -1 means it is not found. account for this 
            split_index = substring.rindex(',', 0, MAX_CHARS) + 1     #add 1 to split after the comma
            new_list.append(substring[:split_index].strip())      
            substring = substring[split_index:]

            index += 1;                 # update index of split

        new_list.append(substring.strip())

    return new_list


def number_of_items(item):
    ''' returns: number of items for that object. Returns 1 if no serial numbers
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
    
#print(intro) todo print 

# prompt user for input excel sheet file name
inventory = get_inventory()
    
#todo options: should have a deployable, or something like that, column for items to add to 1750
#   but could ask user to enter in the sheet name to search, also the column number or names to add data to sheet

# get data from excel sheet
items = get_items_to_print_to_1750(inventory)

# fill in blank serial values in the serial number column with "N/A"

items = items.fillna(value={'SERIAL' : 'N/A'})
#todo allow for blank COMMON NAME 's and replace with NSN name or MPO description
items = items.fillna(value={'COMMON NAME' : items['NSN DESCRIPTION']}) # 

# puts all the items with the same 'common name' on the same line with the serial numbers
items = combine_same_items(items)
#todo change this naming 
items = format_for_1750(items)


#for each item in items 
#add to contents field while there is space
#todo make new page if not space
#add the data to the dict below which will print to the DD-1750
ff = FillableFields()


# Add the inventory items to a FillableFields object so that the items
# are in the proper format to ouput to a PDF
line_num = 1    #start at 1 b/c line num starts at 1
for item in items:  
    # Put total number of items on first line of the items
    count = number_of_items(item) 
    ff.add_total_field(count, line_num)

    # split up the items so that the contents is split over multiple lines
    # if necessary. Otherwise, all items will be on the first line with the 
    # total count
    item_split_list = char_limit_item(item)
    for line in item_split_list:
        ff.add_contents_field(line, line_num)
        line_num += 1   #since contents is split over a line, increment line number

# todo ask  to output dd1750 or da-2062
# todo translate the fields in the excel sheet to the 1750 or 2062 
# todo get correct sum the columns and put total in total_#
# todo prompt user for output filename

# save as new PDF

# below from https://pypdf.readthedocs.io/

pdfOpened = False
pdfFilename  = "DD-Form-1750-Packing-List editable.pdf" #todo change to real filename

reader = PdfReader(pdfFilename)
#while not pdfOpened:
#    # try opening the DD-1750 PDF using the default filename
#    try:
#        reader = PdfReader(pdfFilename)
#        pdfOpened = True
#    except FileNotFoundError: 

#        logging.error("Default filename for opening DD-1750 incorrect")
#        print("DD-1750 Form to output could not be found. Make sure the following PDF is in the same folder \"DD-Form-1750-Packing-List editable\"")
#        #default filename failed, so ask user for filename
#        pdfFilename = input("Enter the full filename to the editable DD-1750 PDF:\n")

writer = PdfWriter()


#print(reader.get_form_text_fields(True))


page = reader.pages[0]   # from https://pypdf.readthedocs.io/
fields = reader.get_fields()     # from https://pypdf.readthedocs.io/


writer.add_page(page)   # from https://pypdf.readthedocs.io/
writer.update_page_form_field_values(writer.pages[0], ff.ff_dict) # from https://pypdf.readthedocs.io/


#todo PermissionError when file open
# write "output" to pypdf-output.pdf # below from https://pypdf.readthedocs.io/
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)

print("DD-1750 successfully outputted") #todo better info needed