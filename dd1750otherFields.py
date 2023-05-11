def prompt_end_item_field(ff):
    ''' returns: FillableFields object
    Adds to FillableFields object with END ITEM information 

    ff: must be a FillableFields object
    '''
    text = input("Enter '3. END ITEM': ")
    ff.add_end_item_field(text)
    return ff

def prompt_no_boxes_field(ff):
    ''' returns: FillableFields object
    Adds to FillableFields object with number of boxes in the set information 

    ff: must be a FillableFields object
    '''
    text = input("Enter '1. NO BOXES': ")
    ff.add_no_boxes_field(text)
    return ff
    

def prompt_date_field(ff):
    ''' returns: FillableFields object
    Adds to FillableFields object with date of preparation 

    ff: must be a FillableFields object
    '''
    text = input("Enter the date prepared: ")
    ff.add_date_field(text)
    return ff
    

def prompt_packed_by_field(ff):
    ''' returns: FillableFields object
    Adds to FillableFields object with name of who packed the items 
        
        Assumes that the individual who package the items is the one who certifies the DD-1750. 
    ff: must be a FillableFields object
    '''
    text = input("Enter name of who packed the items: ")
    ff.add_packed_by_field(text)
    ff.add_certname_field(text)
    return ff
    

def add_other_fields(ff):
    ''' returns: FillableFields object
    Adds to FillableFields object with packed_by, date, no_boxes, and end_items fields filled out. Will prompt user to enter the required text. 
        Note: box number is added with the total number of items and
        completed in a different file. 

    ff: must be a FillableFields object
    '''
    ff = prompt_packed_by_field(ff)
    ff = prompt_date_field(ff)
    ff = prompt_no_boxes_field(ff)
    ff = prompt_end_item_field(ff)
    return ff

    