from flask import Flask, jsonify
import requests

app = Flask(__name__)

health_status = True

@app.route('/', methods=['GET'])
def get_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    if response.status_code == 200:
        fact = response.json().get('fact', 'No fact available')
        return jsonify({'cat_fact': fact})
    else:
        return jsonify({'error': 'Failed to fetch cat fact'}), response.status_code

@app.route('/health')
def health():
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

