# Landscrape
Web-Scraping application that allows a user to find the best things of interest to them in the area

# Overview
Landscrape utilizes a web scraper that returns highly rated attractions in a given geographical radius given a keyword. The application will be implemented with a Python backend which utilizes the Flask microframework.

# Requirements
- Python (2.7.11 or later)
- Flask (0.12.2)

# Initial Set-Up
1. Clone the repository
2. In a terminal, execute `sudo bash start prep`. This will install the necessary dependencies

As mentioned, you can install Flask via pip inside of a Python Virtual Environment. In order to do this,
ensure that you have virtualenv version 15.1.0 or later(you can check with `virtualenv --version`). You can activate
the Virtual Environment by navigating to the `server` folder and typing `source Landscrape/bin/activate`. You can
deactivate the virtualenv at any time using command `deactivate`.

# Running the Application
1. Clone the repository
2. In a terminal, execute `bash start`
3. Navigate the the LocalHost port designated in the terminal to view the site.
4. Click on "About" to view our Code Documentation

# Stuff We Used
- Flask: http://flask.pocoo.org/docs/0.12/
- Doxygen: http://www.stack.nl/~dimitri/doxygen/
- WTForms: https://wtforms.readthedocs.io/
- Yelp: https://www.yelp.com/

# Testing
We utilized Python's Built-In Unit Testing Framework in order to test our scraping functionality. Our test suite file is included in the server folder.

You can look at our testing results by clicking on the "Is Landscrape Complete?" Link in our NavBar. This will initiate the test suite and display the results. 

- Python UnitTest: https://docs.python.org/2/library/unittest.html

# Documentation
You will need to have cloned/forked our repo (which you should have done to run our app).

- Server Documentation: Navigate to `Landscrape/server/html/index.html` and open that file with a browser.
- Scraper Documentation: Navigate to `Landscrape/server/Scraper/html/index.html` and open that file with a browser.

From there you can use the navigation bar and go to `Namespaces` then `Namespace List` click on the bottom-most `server` to see all of our classes, functions, variables, etc.

We used doxygen to generate our documentation. 
