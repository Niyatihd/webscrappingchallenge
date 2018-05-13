from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    marsinfo = mongo.db.marsinfo.find_one()
    return render_template("index.html", marsinfo=marsinfo)


@app.route("/scrape")
def scrape():
    marsinfo = mongo.db.marsinfo
    marsinfo_data = scrape_mars.scrape()
    marsinfo.update(
        {},
        marsinfo_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)