# Recognize
This is the main repository for this project. Below are the steps for setting up to run this project

## Steps - 

1. Install python 3 from website on your machine windows or linux. 

2. For linux machine use python3 in commands in place of python

3. For windows Make sure python is added to your PATH Variable. To check open cmd and type python --version. if it shows version no. then you are set
4. Download the codebase by going to directory where you want to store the codebase then do

    git clone [repository url]

5. open up cmd / shell then type

    cd recognize

6. install necessary packages 

    pip install -r requirements.txt

7. Apply migrations to database 

    python manage.py migrate    

8. To run django development server

    python manage.py runserver