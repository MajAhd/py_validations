<div align="center">

# Py Validations Pure Python Data Validator

![Image](./img/PyValidation.png?raw=true "Elixir Validation")

</div>

---
Simple and easy library to Validate data in python

![example workflow](https://github.com/MajAhd/py_validations/actions/workflows/python-package.yml/badge.svg)


## install

```
  pip install pyvalidations
```

## Usage

--- 

```python
data = {
    "first_name": "Majid"
}

rules = { 
    "first_name": ["required", "string", "max:128"] 
}

PyValidations(data, rules).make()
```

## Documentation

- [Start Validation](https://github.com/MajAhd/py_validations/wiki)
- [Required](https://github.com/MajAhd/py_validations/wiki/Required)
- [Accepted](https://github.com/MajAhd/py_validations/wiki/Accepted)
- [Alpha & String](https://github.com/MajAhd/py_validations/wiki/Alpha-and-String)
- [Boolean](https://github.com/MajAhd/py_validations/wiki/Boolean)
- [Numbers](https://github.com/MajAhd/py_validations/wiki/Numbers)
- [Min & Max](https://github.com/MajAhd/py_validations/wiki/Max-&-Min)
- [Internet](https://github.com/MajAhd/py_validations/wiki/Internet-Address-:-email-,-url-,-ip)
- [In & Not_In](https://github.com/MajAhd/py_validations/wiki/in-&-not-in)
- [UUID](https://github.com/MajAhd/py_validations/wiki/uuid)
- [Date&Time](https://github.com/MajAhd/py_validations/wiki/Date-and-Time)
- [Different](https://github.com/MajAhd/py_validations/wiki/Greater-that-&-Less-Than-&-equal-&-Different-Field)
- [Confirmation](https://github.com/MajAhd/py_validations/wiki/Confirmation)
- [Nullable](https://github.com/MajAhd/py_validations/wiki/Nullable)

## Author

***
Majid Ahmaditabar

PyValidation is released under the [MIT License](https://github.com/MajAhd/py_validations/blob/main/LICENSE).