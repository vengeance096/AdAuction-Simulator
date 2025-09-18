#this is function from flask which will render 
# the index.html , means it will find it in the folders and will render (show it)

from flask import Flask , render_template 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)