#imports from standard python library. 
# os interacts with the operating system, allowing you to interact with file system, read directories, and launch applications.
import os
#import json library for company.json file
import json
#imports the flask class
#imports render_template
from flask import Flask, render_template

#creating instance of it in a variable called 'app'. 
# Only one argument, so can use the python variable __name__.
app = Flask(__name__) 

# @ = pie decorator. A way of wrapping functions.
# When trying to browse root directory ("/"), Flask triggers the index function underneath and returns render_template("index.html").ie displays the home page.
# Flask expects index.html to be inside a file named 'templates' which is on the same level as the run.py file.
@app.route("/")
def index(): # view is called inside html file
    return render_template("index.html")


@app.route("/about")
def about(): # view is called inside html file
    data = []
    with open("data/company.json", "r") as json_data: #"r" = assign
        data = json.load(json_data) # sets our empty 'data' list to equal the parsed JSON data that we've sent through.
    return render_template("about.html", page_title="About", company=data) # new 'company' variable is equal to the list of data being loaded the the json file.


@app.route("/contact")
def contact(): # view is called inside html file
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers(): # view is called inside html file
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": #__main__ is the default module in python
    app.run( # we want to run our app using the arguments inside this statement
        host=os.environ.get("IP", "0.0.0.0"), 
        port=int(os.environ.get("PORT", "5000")),
        debug=True #SHOULD ONLY BE TRUE IN DEVELOPMENT. CHANGE TO FALSE BE SUBMITTING.
    )