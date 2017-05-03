# Electronic Medical Records OneClickVitals
A web application that manages and tracks patient records, developed to facilitate medical doctors and their staff.

The application is developed and tested in a virtual environment. Contributors include Yukhe Lavinia and Sirisha Dumpala. Both contributors share equal role in developing the project. Coding and testing were completed in 2015.


Software requirements:

  Python = 3.4.0

  Django = 1.8.4

The following lists the tests done and the tools used:

  Static unit testing - Pylint

  Dynamic unit testing - Python Unittest

  Functional testing - Selenium IDE and Selenium WebDriver

To run:

  Go to the project root directory
  
  Create virtual environment with python=3.4, django=1.8.4 (assuming Anaconda is installed; otherwise, you can create it using Python virtualenv):
  
    conda create -n newvirenv python=3.4 django=1.8.4  
    
  Activate the virtual environment:
  
    source newvirenv activate 
     
  Then install the following:
  
    easy_install -Z django-registration
    
    pip install django-datetime-widget
    
    pip install django-widget-tweaks
    
    pip install django-localflavor
    
    pip install django-chart-tools
    
    pip install Pillow
    
  Run:
  
    python manage.py runserver

