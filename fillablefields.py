class FillableFields(object):
    MAX_ITEMS = 18

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
    returns: a list of the boxes
    '''
    def get_box_fields(self):
        return self.box

    '''
    returns: True is text for the box field is added to the box list, otherwise false if the length of the box list is greater than MAX_ITEMS
    '''
    def add_box_field(self, text):
        if(len(self.box) < self.MAX_ITEMS):
            self.box.append(text)
            return True
        else:
            return False

    def get_contents_fields(self):
        return self.contents

    '''
    returns: True is text for the contents field is added to the contents list, otherwise false if the length of the contents list is greater than MAX_ITEMS
    '''
    def add_contents_field(self, text):
        if(len(self.contents) < self.MAX_ITEMS):
            self.contents.append(text)
            return True
        else:
            return False

    '''
    returns: a list of the init fields
    '''
    def get_init_fields(self):
        return self.init

    '''
    returns: True is text for the init field is added to the init list, otherwise false if the length of the init list is greater than MAX_ITEMS
    '''
    def add_init_field(self, text):
        if(len(self.init) < self.MAX_ITEMS):
            self.init.append(text)
            return True
        else:
            return False

    '''
    returns: a list of the spares fields
    '''
    def get_spares_fields(self):
        return self.spares

    '''
    returns: True is text for the spares field is added to the spares list, otherwise false if the length of the spares list is greater than MAX_ITEMS
    '''
    def add_spares_field(self, text):
        if(len(self.spares) < self.MAX_ITEMS):
            self.spares.append(text)
            return True
        else:
            return False

    '''
    returns: a list of the total fields
    '''
    def get_total_fields(self):
        return self.total

    '''
    returns: True is text for the total field is added to the total list, otherwise false if the length of the total list is greater than MAX_ITEMS
    '''
    def add_total_field(self, text):
        if(len(self.total) < self.MAX_ITEMS):
            self.total.append(text)
            return True
        else:
            return False

    '''
    returns: a list of the uint fields
    '''
    def get_uint_fields(self):
        return self.uint

    '''
    returns: True is text for the uint field is added to the uint list, otherwise false if the length of the uint list is greater than MAX_ITEMS
    '''
    def add_uint_field(self, text):
        if(len(self.uint) < self.MAX_ITEMS):
            self.uint.append(text)
            return True
        else:
            return False

    #def is_full(self):
    #    return False #todo change so tracks if full

