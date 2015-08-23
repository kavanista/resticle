from flask import Flask, jsonify
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/data')
def getData():
    data = db.get_all()
    print data
    return jsonify({ "data" : data })

if __name__ == '__main__':
    app.run(debug=True)
