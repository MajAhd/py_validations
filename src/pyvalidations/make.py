from .factory import Validate


def make(data, rules):
    """
    make validation
    :return: dictionary
    """
    validate = {
        "failed": False,
        "errors": {}
    }
    for rule in rules:
        key = rule
        rule_value = rules[rule]
        if key in data:
            data_value = data[key]
            result = Validate(key, data_value, rule_value, data).validation()
            if len(result) > 0:
                validate["failed"] = True
                validate["errors"][key] = result
        else:
            validate["failed"] = True
            validate["errors"][key] = [f"The {key} is not exist"]
    return validate
