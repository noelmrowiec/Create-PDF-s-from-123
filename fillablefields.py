class FillableFields(object):
    MAX_ITEMS = 18
    ff_dict = {}

    box = []

    certname = ''

    contents = []

    cur_page = ''
    date = ''
    end_item = ''

    init = []

    no_boxes = ''
    order_no = ''
    packed_by = ''
    req_no = ''

    spares = []

    total = []

    total_pages = ''

    uint = []

    '''
    returns: True is text for the box field is added to the box list, otherwise false if the length of the box list is greater than MAX_ITEMS

    line_num: line number, for 
    '''
    def add_box_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'box_{line_num}'] = text
            return True
        else:
            return False

        

    '''
    returns: True is text for the contents field is added to the contents list, otherwise false if the length of the contents list is greater than MAX_ITEMS
    '''
    def add_contents_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'contents_{line_num}'] = text
            return True
        else:
            return False

    '''
    returns: True is text for the init field is added to the init list, otherwise false if the length of the init list is greater than MAX_ITEMS
    '''
    def add_init_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'init_{line_num}'] = text
            return True
        else:
            return False

    '''
    returns: True is text for the spares field is added to the spares list, otherwise false if the length of the spares list is greater than MAX_ITEMS
    '''
    def add_spares_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'spares_{line_num}'] = text
            return True
        else:
            return False

    '''
    returns: True is text for the total field is added to the total list, otherwise false if the length of the total list is greater than MAX_ITEMS
    '''
    def add_total_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'total_{line_num}'] = text
            return True
        else:
            return False

    '''
    returns: True is text for the uint field is added to the uint list, otherwise false if the length of the uint list is greater than MAX_ITEMS
    '''
    def add_uint_field(self, text, line_num):
        if(line_num < self.MAX_ITEMS):
            self.ff_dict[f'uint_{line_num}'] = text
            return True
        else:
            return False

