from flask import Flask, jsonify, request
from flask_cors import CORS
from modules import constants
from modules import utils


app = Flask(__name__)
CORS(app)


# WEB SERVER


@app.route('/api/')
def index():
    return jsonify({'status': 'alive'})


@app.route('/api/test')
def test():
    return jsonify({'status': 'test'})


@app.route('/api/getabi', methods=['POST'])
def queries():
    data = request.get_json()    
    contract = data.get('contract')
    queries = utils.fetch_abi_info(contract)
    return jsonify(queries)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=constants.PORT)

