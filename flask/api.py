from random import randint, random
import csv
from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def get():
   if request.method == 'POST':
        content = request.json
        content = [content['control']]
        if content[0] == "": return jsonify({'response':'not valid'})
        np.array(content).tofile('control.txt', sep=",")
        return jsonify({'response':'Mass Flow Changed', 'mfv': content})
   else:
        file = open("sample.csv", "r")
        data = list(csv.reader(file, delimiter=","))
        file.close()
        resp = {
            'power': 3, 
            'coreTemp': data[0][7], 
            'coolantTemp': 3
        }
        # return jsonify(resp)
        return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)