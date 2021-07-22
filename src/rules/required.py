class Required:
    def __init__(self, all_data, value, req_field):
        self.all_data = all_data
        self.value = value
        self.req_field = req_field

    def is_required(self):
        if self.value is None or self.value == "":
            return False
        else:
            return True

    def required_if(self):
        return self.value

    def required_unless(self):
        return self.value

    def required_with(self):
        return self.value

    def required_without(self):
        return self.value
