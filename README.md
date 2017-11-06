# Landscrape
Web-Scraping application that allows a user to find the best things of interest to them in the area

# Overview
Landscrape utilizes a web scraper that returns highly rated attractions in a given geographical radius given a keyword. The application will be implemented with a Python backend which utilizes the Flask microframework.

# Requirements
- Python (2.7.11 or later)
- Flask (0.12.2)
- Virtualenv 15.1.0

# Initial Set-Up
1. Clone this Repository and Navigate into `Landscrape/server/`
2. Use the Command `source Landscrape/bin/activate` to launch the Virtual Environment
3. Use Command `pip install flask` to get the Flask Module.
4. Use Command `pip install Flask-WTF` to get the WTForms module.
5. Use Command `pip install bs4` to get the BeautifulSoup module.
6. Use `python server.py` to launch the server, and navigate in a browser to the localhost port indicated 

As mentioned, you can install Flask via pip inside of a Python Virtual Environment. In order to do this,
ensure that you have virtualenv version 15.1.0 or later(you can check with `vitualenv --version`). You can activate
the Virtual Environment by navigating to the `server` folder and typing `source Landscrape/bin/activate`. You can
deactivate the virtualenv at any time using command `deactivate`.

# Running the Application
1. Clone this repository, navigate to `Landscrape/server` and type `python server.py` to run the server
2. Navigate the the LocalHost port designated in the terminal to view the site.
3. Click on "About" to view our Code Documentation

# Stuff We Used
- Flask: http://flask.pocoo.org/docs/0.12/
- Doxygen: http://www.stack.nl/~dimitri/doxygen/
- WTForms: https://wtforms.readthedocs.io/
- Yelp: https://www.yelp.com/

# Documentation
You will need to have cloned/forked our repo (which you should have done to run our app).

- Server Documentation: Navigate to `Landscrape/server/html/index.html` and open that file with a browser. 
- Scraper Documentation: Navigate to `Landscrape/server/Scraper/html/index.html` and open that file with a browser.

From there you can use the navigation bar and go to `Namespaces` then `Namespace List` click on the bottom-most `server` to see all of our classes, functions, variables, etc.
