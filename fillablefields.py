'''
FillableFields class
Author: Noel Mrowiec
Date: 08May2023 

Class is a container for the fillable fields of the DD-1750 PDF. The class has accessor and mutator method to add all fields. The class will limit the number of lines to MAX-ITEMS. After the fields have been added, the ff_dict contains all the fields.
'''


class FillableFields(object):
    MAX_ITEMS = 18
    ff_dict = {}

    #init = [] not used

    
    #order_no = '' not used
    #req_no = ''  not used

    #spares = [] not used

    #uint = [] not used


    def add_certname_field(self, name):
        ''' Adds name to certname field

        name: must be a string
        '''
        self.ff_dict['certname'] = name


    def add_packed_by_field(self, name):
        ''' Adds name to packed_by field

        name: must be a string
        '''
        self.ff_dict['packed_by'] = name

    def add_cur_page_field(self, value):
        ''' Adds number to cur_page field

        value: must be a int
        '''
        self.ff_dict['cur_page'] = value

    def add_date_field(self, value):
        ''' Adds date field

        value: must be a string
        '''
        self.ff_dict['date'] = value


    def add_end_item_field(self, value):
        ''' Adds end_item field

        value: must be a string
        '''
        self.ff_dict['end_item'] = value

    def add_no_boxes_field(self, value):
        ''' Adds end_item field

        value: must be a int
        '''
        self.ff_dict['no_boxes'] = value

    def add_total_pages_field(self, value):
        ''' Adds total_pages field

        value: must be a int
        '''
        self.ff_dict['total_pages'] = value
    
    def add_box_field(self, box_num, line_num):
        '''
        returns: True is text for the box field is added to the box list, otherwise false if the length of the box list is greater than MAX_ITEMS

        box_num: must be integer for box number
        line_num: must be integer (from 1 to 18) with the line number to place 
        '''
        if(line_num <= self.MAX_ITEMS and line_num >= 1):
            self.ff_dict[f'box_{line_num}'] = box_num
            return True
        else:
            return False


    def add_contents_field(self, text, line_num):
        '''
        returns: True is text for the contents field is added to the contents list, otherwise false if the length of the contents list is greater than MAX_ITEMS
        '''
        if(line_num <= self.MAX_ITEMS):
            self.ff_dict[f'contents_{line_num}'] = text
            return True
        else:
            return False

    def add_init_field(self, text, line_num):
        '''
        returns: True is text for the init field is added to the init list, otherwise false if the length of the init list is greater than MAX_ITEMS
        '''
        if(line_num <= self.MAX_ITEMS):
            self.ff_dict[f'init_{line_num}'] = text
            return True
        else:
            return False


    def add_spares_field(self, text, line_num):
        '''
        returns: True is text for the spares field is added to the spares list, otherwise false if the length of the spares list is greater than MAX_ITEMS
        '''
        if(line_num <= self.MAX_ITEMS):
            self.ff_dict[f'spares_{line_num}'] = text
            return True
        else:
            return False

    def add_total_field(self, text, line_num):
        '''
        returns: True is text for the total field is added to the total list, otherwise false if the length of the total list is greater than MAX_ITEMS
        '''
        if(line_num <= self.MAX_ITEMS):
            self.ff_dict[f'total_{line_num}'] = text
            return True
        else:
            return False

    def add_uint_field(self, text, line_num):
        '''
        returns: True is text for the uint field is added to the uint list, otherwise false if the length of the uint list is greater than MAX_ITEMS
        '''
        if(line_num <= self.MAX_ITEMS):
            self.ff_dict[f'uint_{line_num}'] = text
            return True
        else:
            return False

