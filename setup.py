from setuptools import setup, find_packages

setup(
    name='PyValidation',
    version='0.1.0',
    author='Majid Ahmaditabar',
    keywords='validation, data_validator , python_validator ,PyValidation',
    author_email='mjd.ahd.tbr@gmail.com',
    package_dir={'': 'pyvalidation'},
    packages=find_packages(where='pyvalidation'),
    # packages=['PyValidation', 'PyValidation.tests'],
    scripts=['bin/script1', 'bin/script2'],
    url='http://pypi.python.org/pypi/PyValidation/',
    project_urls={
        'Bug Reports': 'https://github.com/MajAhd/py_validation/issues',
        'Source': 'https://github.com/MajAhd/py_validation/',
        'Wiki': 'https://github.com/MajAhd/py_validation/wiki',
    },
    license='LICENSE',
    description='Simple and easy library to Validate data in Python',
    long_description=open('readme.md').read() + '\n \n' + open('CHANGELOG.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI   Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.10, <6',
    install_requires=[
        "pytest",
    ],
)
