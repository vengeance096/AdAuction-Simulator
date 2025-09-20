# Flask app for ad-auction simulator
# This renders index.html and provides ads data for bidding system
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ads")
def ads():
    ads_data = [
        {"brand": "Nike", "price": 100, "message": "Nike, just do it!"},
        {"brand": "Adidas", "price": 90, "message": "Impossible is nothing."},
        {"brand": "Puma", "price": 10, "message": "Forever Faster."}
    ]
    return jsonify({"ads": ads_data})

@app.route("/FAQ")
def contact():
    return render_template("FAQ.html")

if __name__ == "__main__":
    app.run(debug=True)