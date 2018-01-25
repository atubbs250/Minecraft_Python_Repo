from flask import Flask
app = Flask(__name__)

@app.route("/")
def showName():
    return "Amanda Tubbs"

app.run()
