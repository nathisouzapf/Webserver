from flask import Flask, request, jsonify
from db import create_table
from service import insert_data, get_all_data
from login import generate_token, token_required

app = Flask(__name__)

create_table()

# 🔐 LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "123":
        token = generate_token(username)
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


# 🔒 ROTA PRINCIPAL
@app.route('/', methods=['POST', 'GET'])
@token_required
def use_api():
    try:
        if request.method == "POST":
            value = request.json.get('data')

            if value is None:
                return jsonify({"error": "No value provided"}), 400

            insert_data(value)

            return jsonify({"message": "Value added successfully"}), 201

        elif request.method == "GET":
            values = get_all_data()
            return jsonify(values), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="10.1.24.49", port=5000, debug=True)