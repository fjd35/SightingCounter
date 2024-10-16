from flask import Flask, render_template, request, redirect, url_for 
import json

app = Flask(__name__) 

DATA_FILE = "data.json"

@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route("/add_sighting", methods=["POST"])
def add_sighting():
    location = request.form.get("location")
    data = get_data()
    data.setdefault(location, 0)
    data[location] += 1
    save_data(data)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


def get_data() -> dict:
    with open(DATA_FILE) as f:
        data = json.load(f)
    return data

def save_data(data: dict):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

if __name__ == "__main__": 
    app.run(debug=True) 
