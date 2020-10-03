from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Scrape_Mars
import Scrape_facts

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_app"
mongo = PyMongo(app)


@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()

    return render_template("index.html", destin=destination_data)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    Mars_data = Scrape_Mars.scrape_info()
    #Mars_data = Scrape_facts.scrape_info()
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({},Mars_data,upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
