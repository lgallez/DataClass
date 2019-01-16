from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
mars = scrape_mars

# mongo = PyMongo(app)

#  create route that renders index.html template
@app.route("/")
def index():
    
    return render_template("index.html", mars=mars)




if __name__ == "__main__":
    app.run(debug=True)
