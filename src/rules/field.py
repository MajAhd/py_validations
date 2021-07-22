class Field:
    def __init__(self, all_data, req_field):
        self.all_data = all_data
        self.req_field = req_field

    def field_exist(self):
        return self.req_field
