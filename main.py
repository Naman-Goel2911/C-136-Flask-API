from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')

def index():
    return jsonify({
        'data': data,
        'message': 'Success!'
    }), 200

@app.route('/star')

def planet():
    name = request.args.get('star_name')
    star_data = next(item for item in data if item['star_name'] == name)
    return jsonify({
        'data': star_data,
        'message': 'Success!'
    }), 200

app.run()