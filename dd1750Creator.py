'''
DD-1750 Creator Main application
author: Noel Mrowiec
Date: 18April2023  

Creates DD-1750 PDF (packing list) from 123 excel sheet (electronic inventory spreadsheet). 
Requirements: place the included DD-1750 PDF in the same folder as program because it is unprotected, and specific field names are used by the program to fill out the PDF. Additionally, the 123 excel spreadsheet must have the following fields exactly as shown: 'COMMON NAME' and 'SERIAL' for the items and 'PRINT TO DD-1750'. If there is nothing listed in the �COMMON NAME� header, the program will pull from the 'NSN DESCRIPTION'. The program will add the information from the excel sheet if the is a 'x' (lower case x) in the 'PRINT TO DD-1750' column. The name as serial number of the selected items (items with the 'x') will be added to the DD-1750 PDF. The program will automatically combine items with the same common name if there are repeated items. Items with the same name will be added and will be shown in the total's column. The program prompts the user to enter the other information not found in the 123 sheet.

Current version limitations:
-The program cannot work with excel sheet with special formatting to the line header line (which has �COMMON NAME� listed).
to select a print. 
-Currently, a second page of the DD-1750 cannot be created if there are too many items. The user will be warned if the case occurs. 
- If a items doesn�t have a serial number, N/A will be listed for each item.  

'''

import logging
import sys
logging.basicConfig(filename='dd1750CreatorLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
try:
    from fillablefields import FillableFields
    from dd1750HelperFunctions import *
    from dd1750otherFields import *
    from pypdf import PdfReader, PdfWriter      

except:
    logging.critical("Library imports failed")
    print("Unable to import 3rd party libraries. Check that pypdf and pandas and installed.")
    sys.exit()



    
#print(intro) todo print 
print("Welcome to 123 to DD-1750 creator \nBefore beginning, please make sure you have the 123 excel sheet and editable DD-1750 in the same file as the program. The DD-1750 should be bundled with the program. (Note: The DD-1750 cannot be the form from military website since those forms are secured and have different settings).\n")

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
items_list = format_for_1750(items)


#for each item in items 
#add to contents field while there is space
#todo make new page if not space
#add the data to the object below which will print to the DD-1750
ff = FillableFields()

ff = add_other_fields(ff)

add_success,ff = add_inventory_to_FillableFields(items_list, ff)
if(add_success == False):
    print("Warning: You have too many items. Reduce the amount of items to get them all on the same page. Program will continue but will not contain all items")


# todo ask  to output dd1750 or da-2062
# todo translate the fields in the excel sheet to the 1750 or 2062 
# todo get correct sum the columns and put total in total_#
# todo prompt user for output filename


# Save as new PDF
# below from https://pypdf.readthedocs.io/

reader = openPDFfile()

writer = PdfWriter()        #Use writer to write data

#print(reader.get_form_text_fields(True))

page = reader.pages[0]              # Use the first page from the PDF which was read
fields = reader.get_fields()        # fields are the fillable fields of the PDF 


writer.add_page(page)   # from https://pypdf.readthedocs.io/
writer.update_page_form_field_values(writer.pages[0], ff.ff_dict) # writes the data from the FillableField class to the PDF to write


writeToPDF(writer)

print("DD-1750 successfully outputted") #todo better info needed