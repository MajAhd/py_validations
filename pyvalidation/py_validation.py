class PyValidation:
    """@doc
     data ={
       name: "Majid",
       age: 34
     }
     role = {
       name: ["required" , "max:20" , "alpha"],
       age: ["required" ,"numeric", "min:18" , "max:50"
     }
     validator = PyValidation(data, role)

    """

    def __init__(self, data, rules):
        self.rules = rules
        self.data = data

    def make(self):
        for name in self.data:
            data_name = name
            data_val = self.data[name]
            if data_name in self.rules:
                print("data is {0} value {1}".format(data_name, data_val))
            else:
                print("field {0} not found".format(data_name))
