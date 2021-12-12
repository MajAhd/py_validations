from setuptools import setup, find_packages

setup(
    name='PyValidations',
    version='0.3.0',
    author='Majid Ahmaditabar',
    keywords='validation, data_validator , python_validator ,PyValidations',
    author_email='mjd.ahd.tbr@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='http://pypi.python.org/pypi/PyValidations/',
    project_urls={
        'Bug Reports': 'https://github.com/MajAhd/py_validations/issues',
        'Source': 'https://github.com/MajAhd/py_validations/',
        'ChangeLog': 'https://github.com/MajAhd/py_validations/blob/master/CHANGELOG.md',
        'Wiki': 'https://github.com/MajAhd/py_validations/wiki',
    },
    license='MIT',
    description='Simple and easy library to Validate data in Python',
    long_description=open('readme.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.10, <6',
    install_requires=[
        "pytest",
    ],
)
