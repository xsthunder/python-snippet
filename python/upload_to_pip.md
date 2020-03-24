# upload to pip

1. before using auto deployment such as travis, manually upload the first version.
1. setup `.pypirc` instead of `.piprc` see [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account)
1. build package
1. use `python -m twine upload .\dist\*` rather than `python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

build
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

