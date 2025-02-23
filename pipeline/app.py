from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/catfact', methods=['GET'])
def get_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    if response.status_code == 200:
        fact = response.json().get(response.content)
        return jsonify({'cat_fact': fact})
    else:
        return jsonify({'error': 'Failed to fetch cat fact'}), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
