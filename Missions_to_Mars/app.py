from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of Flask
app = Flask(__name__)

# Pymongo to establish connection with MongoDB (setting inline)
# We do it here instead of in the ipynb
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    scraped_info = mongo.db.scraped_info.find_one()

    # Return template and data
    return render_template("index.html", scraped_info=scraped_info)

@app.route("/scrape")
def scraper():
    
    # Run scrape function
    mars_data = scrape_mars.scrape()

    # Update mars_db using update and upsert
    mongo.db.scraped_info.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
