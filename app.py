from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Azure project"
@app.route("/about")
def about():
    return "about section"
if __name__ == "__main__":
    app.run()
