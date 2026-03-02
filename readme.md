## first things first:

When using external dependencies (libraries installed with PIP), it is best to use a python virtual enviroment (venv) to create isolated enviroments and avoid conflicts between projects.

## What is PIP?

- "Prefered installation program" - package manager for python.
- Downloads and adds to your program, third party libararies from PyPI - Python Package Index.

## Why use venv?

- When using Pip, you don't want to create version conflicts in your system - so you install dependencies at the project level.
- Venv is essentially a project level copy of python.

## Setting us a venv?

- In the terminal type `python -m venv venv` - or `python -m venv my_venv_folder`
    - This creates a folder named venv containing the isolated enviroment.
- Now we have the recources for a virtual enviroment, but we have not activated it yet (so any installs would still be global).
- Activate the enviroment with (in windows) `venv/Scripts/activate`
    - You should then see something like `(venv) C:\Path\To\Your\Projects>`
- When you are done working in your virual enviroment, you can exit it with `deactivate`

#### Freezing Requirements

- You should gitignore your `venv` folder, but you want to keep track of what needs installed for your program (whatever you pip installed)
    - To do this, you use a requirements.txt file. You can create it (while the venv is going) with `pip freeze > requirements.txt`
      - This will create a `requirements.txt` file.

#### Installing from requirements.txt

- If you pull your project down from github or other source control, you will need to create the virtual enviroment (you should so this), then you can install all dependencies with `pip install -r requirements.txt`

## PyQt5 - What is it?

- PyGT5 is apopular python library for creating Graphical User Interfaces (GUIs)

### Install PyQt5

- `pip install PYQt5`
- Make sure you are in your virtual enviroment.

### Freeze the requirements

- `pip freeze > requirements.txt`
    - This will create or update your requirements.txt file

