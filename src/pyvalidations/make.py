import src.pyvalidations.factory as Factory


def make(data, rules):
    """
    make validation
    :return: dictionary
    """
    validate = {
        "failed": False,
        "errors": {}
    }
    for name in data:
        key = name
        value = data[name]
        if key in rules:
            result = Factory.Validate(key, value, rules[key], data).validation()
            if len(result) > 0:
                validate["failed"] = True
                validate["errors"][key] = result
    return validate
