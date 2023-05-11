def add_end_item_field(ff):
    '''returns: FillableFields object with END ITEM information added

    ff: must be a FillableFields object
    '''
    text = input("Enter '3. END ITEM': ")
    ff.end_item = text
    return ff

def add_no_boxes_field(ff):
    '''returns: FillableFields object with number of boxes in the set information added

    ff: must be a FillableFields object
    '''
    text = input("Enter '1. NO BOXES': ")
    ff.no_boxes = text
    return ff

def add_box_number_field(ff):
    '''returns: FillableFields object with box number for items information added.

    ff: must be a FillableFields object
    '''
    text = input("Enter the box number for the items: ")
    for i in range(ff.MAX_ITEMS):
        ff.add_box_field(text)
    return ff

def add_date_field(ff):
    '''returns: FillableFields object with date of preparation added

    ff: must be a FillableFields object
    '''
    text = input("Enter the date prepared: ")
    ff.date = text
    return ff

def add_packed_by_field(ff):
    '''returns: FillableFields object with name of who packed the items added
        
        Assumes that the individual who package the items is the one who certifies the DD-1750. 
    ff: must be a FillableFields object
    '''
    text = input("Enter name of who packed the items: ")
    ff.packed_by = text
    ff.certname = text
    return ff

def add_other_field(ff):
    ''' returns: FillableFields object with packed_by, date, box number, no_boxes, and end_items fields filled out. Will prompt user to enter the required text

    ff: must be a FillableFields object
    '''
    ff = add_packed_by_field(ff)
    ff = add_date_field(ff)
    ff = add_no_boxes_field(ff)
    ff = add_box_number_field(ff)
    ff = add_end_item_field(ff)

    return ff