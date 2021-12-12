<div align="center">

# Py Validations Pure Python Data Validator

![Image](https://github.com/MajAhd/py_validations/blob/master/img/PyValidation.png?raw=true "Elixir Validation")

</div>

---
Simple and easy library to Validate data in python

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/PyValidations)](https://pypi.python.org/pypi/PyValidations/)
![example workflow](https://github.com/MajAhd/py_validations/actions/workflows/python-package.yml/badge.svg)
[![PyPI download total](https://img.shields.io/pypi/dm/PyValidations)](https://pypi.python.org/pypi/PyValidations/)
[![PyPI license](https://img.shields.io/pypi/l/PyValidations)](https://pypi.python.org/pypi/PyValidations/)

## install

```
  pip install PyValidations
```

## Usage

--- 

```python
import pyvalidations as PyValidations

data = {
    "first_name": "Majid"
}

rules = {
    "first_name": ["required", "string", "max:128"]
}

PyValidations.make(data, rules)

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
- [File](https://github.com/MajAhd/py_validations/wiki/File)

## Author

***
Majid Ahmaditabar

PyValidations is released under the [MIT License](https://github.com/MajAhd/py_validations/blob/main/LICENSE).