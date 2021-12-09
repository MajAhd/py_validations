<div align="center">

# Py Validation Pure Python Data Validator

![Image](./img/PyValidation.png?raw=true "Elixir Validation")

</div>

---
Simple and easy library to Validate data in python

![example workflow](https://github.com/MajAhd/py_validation/actions/workflows/python-package.yml/badge.svg)


## install

```
  pip install pyvalidation
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

PyValidation(data, rules).make()
```

## Documentation

- [Start Validation](https://github.com/MajAhd/py_validation/wiki)
- [Required](https://github.com/MajAhd/py_validation/wiki/Required)
- [Accepted](https://github.com/MajAhd/py_validation/wiki/Accepted)
- [Alpha & String](https://github.com/MajAhd/py_validation/wiki/Alpha-and-String)
- [Boolean](https://github.com/MajAhd/py_validation/wiki/Boolean)
- [Numbers](https://github.com/MajAhd/py_validation/wiki/Numbers)
- [Min & Max](https://github.com/MajAhd/py_validation/wiki/Max-&-Min)
- [Internet](https://github.com/MajAhd/py_validation/wiki/Internet-Address-:-email-,-url-,-ip)
- [In & Not_In](https://github.com/MajAhd/py_validation/wiki/in-&-not-in)
- [UUID](https://github.com/MajAhd/py_validation/wiki/uuid)
- [Date&Time](https://github.com/MajAhd/py_validation/wiki/Date-and-Time)
- [Different](https://github.com/MajAhd/py_validation/wiki/Greater-that-&-Less-Than-&-equal-&-Different-Field)
- [Confirmation](https://github.com/MajAhd/py_validation/wiki/Confirmation)
- [Nullable](https://github.com/MajAhd/py_validation/wiki/Nullable)

## Author

***
Majid Ahmaditabar

PyValidation is released under the [MIT License](https://github.com/MajAhd/py_validation/blob/main/LICENSE).