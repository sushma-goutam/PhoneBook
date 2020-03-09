![Django CI](https://github.com/sushma-goutam/PhoneBook/workflows/Django%20CI/badge.svg?branch=master)

# Django PhoneBook

A PhoneBook created with Django. It allows you to create, update, retrieve and delete a contact.

Since, this is already implementing Database CRUD operations, this is a good candidate for developing a Project using Rest API.

## How to create a wheel for Django project
I am using 'setuptools_scm' which already tracks files committed to scm. Therefore, we don't need to use 'MANIFEST.in' file for copying files or directories.

### Instructions

* Create a virtual environment and activate it
```
  python -m virtualenv env
  env\Scripts\activate
```

* Create a wrapper for ```manage.py file``` 

  Name this file as ```__main.py__``` and add below content to it-
```
  import os
  from django.core.management import execute_from_command_line


  def main():
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.PhoneBook.settings')
      execute_from_command_line()


  if __name__ == "__main__":
      main()
```

  Notice that we have modified the setting file path to match with the installed folder structure.

* Create a universal wheel
```
python setup.py bdist_wheel --universal
```

* Install wheel in virtual environment
```
  pip install "dist\PhoneBook-0.1.dev8+g1e0cecb.d20200309-py2.py3-none-any.whl"
``` 

* Verify that project files are copied to ```env\Lib\site-packages``` folder

* Start Django server using command ```python -m src.__main__ runserver```
```
  (env) C:\Sushma>python -m src.__main__ runserver
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  March 09, 2020 - 17:07:34
  Django version 3.0.2, using settings 'src.PhoneBook.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
``` 

* Verify in Web Browser

  Navigate to ```http://127.0.0.1:8000/``` and verify that your application is working as expected.