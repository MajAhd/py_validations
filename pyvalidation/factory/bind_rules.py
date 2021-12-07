import pyvalidation.rules as Rules


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
            case "accepted":
                return Rules.Accepted(value).is_accepted()
            case "boolean":
                return Rules.Boolean(value).is_boolean()
            case "confirmed":
                confirmed_name = f"{key}_confirmation"
                if Rules.Field(self.all_data, confirmed_name).field_exist():
                    target = self.all_data[confirmed_name]
                    return Rules.Confirmation(value, target)
                return False
            case "date":
                return Rules.DateTime(value).is_date()
            case "time":
                return Rules.DateTime(value).is_time()
            case "datetime":
                return Rules.DateTime(value).is_date_time()
            case "timezone":
                return Rules.DateTime(value).is_timezone()
            case "date_equals":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).date_equals(self.rule_val)
                return False
            case "after":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_after(self.rule_val)
                return False
            case "after_or_equal":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_after_or_equal(self.rule_val)
                return False
            case "before":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_before(self.rule_val)
                return False
            case "before_or_equal":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_before_or_equal(self.rule_val)
                return False
            case _:
                return "Validation Not Defined!"
