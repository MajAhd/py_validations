from .bind_rules import BindRules
from .bind_exception import BindException


class Validate:
    """
    Data Validation factory
    """

    def __init__(self, key, value, rules, all_data):
        self.__key = key
        self.__value = value
        self.__rules = rules
        self.__all_data = all_data

    def validation(self):
        """
        do validate by rule on data and return message if failed
        :return: dict
        """
        messages = []

        if "nullable" in self.__rules and (self.__value == "" or self.__value is None):
            return messages

        for rule in self.__rules:
            split_rule = rule.split(":")
            rule = split_rule[0]
            rule_value = None if len(split_rule) < 2 else split_rule[1]
            # Required
            if rule == "required_if":
                is_required_if = BindRules("required_if", rule_value, self.__all_data).build(self.__key, self.__value)
                if is_required_if:
                    is_passed = BindRules("required", rule_value, self.__all_data).build(self.__key, self.__value)
                    if not is_passed:
                        messages.append(BindException(self.__key, rule_value).build(rule))
                else:
                    return []

            if rule == "required_unless":
                is_required_unless = BindRules("required_unless", rule_value, self.__all_data).build(self.__key, self.__value)
                if is_required_unless:
                    is_passed = BindRules("required", rule_value, self.__all_data).build(self.__key, self.__value)
                    if not is_passed:
                        messages.append(BindException(self.__key, rule_value).build(rule))
                else:
                    return []

            is_passed = BindRules(rule, rule_value, self.__all_data).build(self.__key, self.__value)
            if not is_passed:
                messages.append(BindException(self.__key, rule_value).build(rule))
        return messages
