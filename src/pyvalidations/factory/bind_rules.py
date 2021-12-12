from .. import rules as Rules


class BindRules:
    """
     Bind Validation Rules from /rules
     :param rule validate name and the rule of validate
     :param rule_val validate default value ro further process
     :param all_data all data inside the validation request
    """

    def __init__(self, rule, rule_val, all_data):
        self.rule = rule
        self.rule_val = rule_val
        self.all_data = all_data

    def build(self, key, value):
        """
        base on rule bind and run validation
        :param key: data name
        :param value: data value
        :return: Boolean
        """
        match self.rule:
            case "required":
                return Rules.Required(value).is_required()
            case "required_if":
                return Rules.Required(value, self.all_data).required_if(self.rule_val)
            case "required_unless":
                return Rules.Required(value, self.all_data).required_unless(self.rule_val)
            case "required_with":
                return Rules.Required(value, self.all_data).required_with(self.rule_val)
            case "required_without":
                return Rules.Required(value, self.all_data).required_without(self.rule_val)
            case "accepted":
                return Rules.Accepted(value).is_accepted()
            case "boolean":
                return Rules.Boolean(value).is_boolean()
            case "confirmed":
                confirmed_name = f"{key}_confirmation"
                if Rules.Field(self.all_data, confirmed_name).field_exist():
                    target = self.all_data[confirmed_name]
                    return Rules.Confirmation(value, target).is_confirmed()
                return False
            # String And Alpha
            case "string":
                return Rules.Alpha(value).is_string()
            case "alpha":
                return Rules.Alpha(value).is_alpha()
            case "start_with":
                if Rules.Alpha(value).is_string():
                    return Rules.Alpha(value).start_with(self.rule_val)
                return False
            case "end_with":
                if Rules.Alpha(value).is_string():
                    return Rules.Alpha(value).end_with(self.rule_val)
                return False
            # Date Time Validation
            case "date":
                return Rules.DateTime(value).is_date()
            case "time":
                return Rules.DateTime(value).is_time()
            case "datetime":
                return Rules.DateTime(value).is_date_time()
            case "timezone":
                return Rules.DateTime(value).is_timezone()
            case "date_equals":
                if Rules.DateTime(self.rule_val).is_date() and Rules.DateTime(value).is_date():
                    return Rules.DateTime(value).date_equals(self.rule_val)
                return False
            case "after":
                if Rules.DateTime(self.rule_val).is_date() and Rules.DateTime(value).is_date():
                    return Rules.DateTime(value).is_after(self.rule_val)
                return False
            case "after_or_equal":
                if Rules.DateTime(self.rule_val).is_date() and Rules.DateTime(value).is_date():
                    return Rules.DateTime(value).is_after_or_equal(self.rule_val)
                return False
            case "before":
                if Rules.DateTime(self.rule_val).is_date() and Rules.DateTime(value).is_date():
                    return Rules.DateTime(value).is_before(self.rule_val)
                return False
            case "before_or_equal":
                if Rules.DateTime(self.rule_val).is_date() and Rules.DateTime(value).is_date():
                    return Rules.DateTime(value).is_before_or_equal(self.rule_val)
                return False
            # different Validation
            case "different":
                return Rules.Different(value).is_different(self.rule_val)
            case "equal":
                return Rules.Different(value).is_equal(self.rule_val)
            case "gt":
                return Rules.Different(value).gt(self.rule_val)
            case "gte":
                return Rules.Different(value).gte(self.rule_val)
            case "lt":
                return Rules.Different(value).lt(self.rule_val)
            case "lte":
                return Rules.Different(value).lte(self.rule_val)
            # Inside
            case "in":
                return Rules.Inside(value).is_in(self.rule_val)
            case "not_in":
                return Rules.Inside(value).is_not_in(self.rule_val)
            # Internet
            case "email":
                return Rules.Internet(value).email()
            case "url":
                return Rules.Internet(value).url()
            case "ip":
                return Rules.Internet(value).ip()
            case "ipv4":
                return Rules.Internet(value).ipv4()
            case "ipv6":
                return Rules.Internet(value).ipv6()
            #  Max Min
            case "max":
                return Rules.Max(value).is_maximum(self.rule_val)
            case "min":
                return Rules.Min(value).is_minimum(self.rule_val)
            # Number
            case "numeric":
                return Rules.Number(value).is_numeric()
            case "digits":
                return Rules.Number(value).digits(self.rule_val)
            # UUID
            case "uuid":
                return Rules.Uuid(value).is_uuid()
            # File
            case "file":
                return Rules.Storage(value).is_file()
            case "mimes":
                return Rules.Storage(value).mimes(self.rule_val)
            case "mime_types":
                return Rules.Storage(value).mime_types(self.rule_val)
            case "max_size":
                return Rules.Storage(value).max_size(self.rule_val)
            case "min_size":
                return Rules.Storage(value).min_size(self.rule_val)
            case _:
                return "Validation Not Defined!"
