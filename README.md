The Pineapple Project
======================
The Pineapple Project is an open source argiculture recommendation system.

Setting Up for Local Development
--------------------------------
###Prerequisites
To build The Pineapple Project locally you'll need

- [python 2.7](https://pypi.python.org/pypi/virtualenv)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [PostgreSQL](http://www.postgresql.org/download/)

Then follow these instructions

1. Clone the repo
1. Create a virtual environment in the new directory

       virtualenv venv --distrubute   
1. Activate the virtual environment
        
        #bash
        source venv/bin/activate
        
        #powershell
        . ./venv/Scripts/activate.ps1
1. Install the requirements

        pip install -r requirements.txt
1. Set environment variables
        
        # bash
        export DJANGO_SECRET_KEY=YourLocalSecretKey
        
        # powershell
        $Env:DJANGO_SECRET_KEY = "YourLocalSecretKey"
1. Run the development server

        #bash
        python manage.py runserver --settings=ThePineappleProject.settings.local
