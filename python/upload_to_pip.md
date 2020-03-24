# upload to pip

## setup.py

1. only a limited list of file will be automatically added, [distutils - Including non-Python files with setup.py - Stack Overflow](https://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py).

2. only dir includes `__init__.py` will be recognized as packages and added to path.

## locally

1. ~~before using auto deployment such as travis, manually upload the first version.~~
1. setup `.pypirc` instead of `.piprc` see [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account)
1. build package
1. use `python -m twine upload .\dist\*` rather than `python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

## use travis delpoyment

1. generate secure key for different repo [PyPI deployment - Travis CI](https://docs.travis-ci.com/user/deployment/pypi/). notes that may use the same (global) pypi key, but secure key differs from different project or the current timestamp.
  1. when using interactive windows cmd for gem, it seems like pypi key were chunked. dont insert the pypi key in the middle of the command. input the command in sequence and double check the command using up arrow after excution.
  2. paste pypi key including `pypi-` prefix.

build and install
-----
```ps
# run by powershell

# deps
# for packaging
# pip install setuptools wheel twine # --user
# for uploading
# pip install --user --upgrade twine

# building
$ErrorActionPreference = "Stop" # exit on error

$version=get-content ./config/version.txt
$project_name=get-content ./config/project_name.txt

pip uninstall $project_name -y
python setup.py sdist bdist_wheel
pip install .\dist\$project_name-$version-py3-none-any.whl

```

ref 
-----
[Packaging Python Projects — Python Packaging User Guide](http://packaging.python.org/tutorials/packaging-projects/)

