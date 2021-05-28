from flask import Flask,render_template
import os 
# template_dir = os.path.abspath('multani.tech/front-end)  
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()