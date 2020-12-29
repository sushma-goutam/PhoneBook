![Django CI](https://github.com/sushma-goutam/PhoneBook/workflows/Django%20CI/badge.svg?branch=master)

# Django PhoneBook

A PhoneBook created with Django. It allows you to create, update, retrieve and delete a contact.

### REST APIs
This project also uses Django REST Framework and provides REST APIs for Database CRUD operations.

The REST APIs can be tested in two different ways -

#### Using A WEB UI
- Implemented with REST Framework APIView
- Swagger is also integrated with this project and provides an aditional option for testing APIs.

#### Headless testing
- Implemented with Python's requests library 

## Creating a wheel for Django project

* Create a virtual environment and activate it
```bash
  python -m virtualenv env
  env\Scripts\activate
```

* Create a wrapper for ```manage.py file``` 

  Name this file as ```__main.py__``` and add below content to it-
```bash
  import os
  from django.core.management import execute_from_command_line


  def main():
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.PhoneBook.settings')
      execute_from_command_line()


  if __name__ == "__main__":
      main()
```

  Notice that we have modified the setting file path to match with the installed folder structure.

* Create a setup file for packaging Django project

'setuptools_scm' can tracks files which are already committed to scm. 
Therefore, there is no need to use 'MANIFEST.in' file for copying files or directories.

* Create a universal wheel
```bash
python setup.py bdist_wheel --universal
```

* Install wheel in virtual environment
```bash
  pip install "dist\PhoneBook-0.1.dev8+g1e0cecb.d20200309-py2.py3-none-any.whl"
``` 

* Verify that project files are copied to ```env\Lib\site-packages``` folder

* Start Django server using command ```python -m src.__main__ runserver```
```bash
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
  
### Running Django project inside docker container

Build container

    docker-compose build  
    
Start Container

    docker-compose up

Open a web browser and navigate to ```http://localhost:8080/```        
