from flask import Flask
from flask import render_template, jsonify
import json,os
app = Flask(__name__)

directory = os.getcwd()
"""
@app.route('/data_json')
def data_json():
    with open(directory + "/LiveSportsWebsite/data.json") as jsonFile:
        jsonObject = json.load(jsonFile)
    return jsonify(jsonObject)
"""
@app.route('/data_json')
def data_json():
    with open(directory + "/LiveSportsWebsite/data.json") as jsonFile:
        jsonObject = json.load(jsonFile)
    
    
    
    
    return jsonify(jsonObject)




@app.route('/')
def index():
    dummy_data = data_json()
    return render_template(
        'index.html',
        matches=dummy_data.json,
    )


if __name__ == "__main__":  
    app.run()
