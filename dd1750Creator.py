from csv import excel_tab
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

# prompt user for input excel sheet file name
while True:
    sheet_filename = input("Enter file name of valid excel sheet (must be a \"123 Sheet\"): ")
    try:
        inventory = pd.read_excel(sheet_filename)
        
    except:
        print('You entered "' + str(sheet_filename) + '", file name not found. Check file name.')
        continue
    else:
        break       #found valid excel sheet
    
print(inventory.head(2))

# open file in try-except

#options: should have a deployable, or something like that, column for items to add to 1750
#   but could ask user to enter in the sheet name to search, also the column number or names to add data to sheet
# get data from excel sheet
# ask  to output dd1750 or da-2062
# translate the fields in the excel sheet to the 1750 or 2062 
# sum the columns and put total in total_#
# prompt user for output filename
# check valid
# save as new PDF

# below from https://pypdf.readthedocs.io/
reader = PdfReader("DD-Form-1750-Packing-List different version.pdf")
writer = PdfWriter()


print(reader.get_form_text_fields(True))


page = reader.pages[0]   # from https://pypdf.readthedocs.io/
fields = reader.get_fields()     # from https://pypdf.readthedocs.io/




fillable_fields_dict = {'box_1': '', 'contents_1': '', 'unit_1': '', 'init_1': '', 'box_2': '', 'contents_2': '', 'unit_2': '', 'init_2': '', 'spares_2': '', 'box_3': '', 'contents_3': '', 'unit_3': '', 'init_3': '', 'spares_3': '', 'box_4': '', 'contents_4': '', 'unit_4': '', 'init_4': '', 'spares_4': '', 'box_5': '', 'contents_5': '', 'unit_5': '', 'init_5': '', 'spares_5': '', 'contents_6': '', 'unit_6': '', 'init_6': '', 'spares_6': '', 'box_6': '', 'init_7': '', 'spares_7': '', 'box_7': '', 'contents_7': '', 'unit_7': '', 'box_8': '', 'contents_8': '', 'unit_8': '', 'init_8': '', 'spares_8': '', 'box_9': '', 'contents_9': '', 'unit_9': '', 'init_9': '', 'spares_9': '', 'box_10': '', 'contents_10': '', 'unit_10': '', 'init_10': '', 'spares_10': '', 'box_11': '', 'contents_11': '', 'unit_11': '', 'init_11': '', 'spares_11': '', 'box_12': '', 'contents_12': '', 'unit_12': '', 'init_12': '', 'spares_12': '', 'box_13': '', 'contents_13': '', 'unit_13': '', 'init_13': '', 'spares_13': '', 'box_14': '', 'contents_14': '', 'unit_14': '', 'init_14': '', 'spares_14': '', 'box_15': '', 'contents_15': '', 'unit_15': '', 'init_15': '', 'spares_15': '', 'box_16': '', 'contents_16': '', 'unit_16': '', 'init_16': '', 'spares_16': '', 'box_17': '', 'contents_17': '', 'unit_17': '', 'init_17': '', 'spares_17': '', 'box_18': '', 'contents_18': '', 'unit_18': '', 'init_18': '', 'spares_18': '', 'certname': '', 'end_item': '', 'packed_by': '', 'no_boxes': '', 'req_no': '', 'order_no': '', 'date': '', 'total_pages': '', 'spares_1': '', 'cur_page': '', 'total_1': '', 'total_2': '', 'total_3': '', 'total_6': '', 'total_4': '', 'total_5': '', 'total_7': '', 'total_8': '', 'total_9': '', 'total_10': '', 'total_11': '', 'total_12': '', 'total_13': '', 'total_14': '', 'total_15': '', 'total_16': '', 'total_17': '', 'total_18': ''}
writer.add_page(page)   # from https://pypdf.readthedocs.io/
writer.update_page_form_field_values(writer.pages[0], fillable_fields_dict) # from https://pypdf.readthedocs.io/



# write "output" to pypdf-output.pdf # below from https://pypdf.readthedocs.io/
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)