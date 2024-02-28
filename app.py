from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__, static_folder='web')

@app.route("/")
def index_page():
    return send_from_directory('web', 'index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    result = 0
    if 'num1' in data and 'num2' in data and 'operation' in data:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing data'}), 400