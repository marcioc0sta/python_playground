from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/sum', methods=['POST'])
def sum_numbers():
    usr_input = request.get_json()

    if "y" not in usr_input:
        return "ERROR", 305

    res = {
        "z": usr_input['x'] + usr_input['y']
    }

    return jsonify(res), 200


@app.route('/json')
def demo_json():
    ret = {
        'field1': ["abc", "def"],
        'field2': True,
        'field3': False,
    }

    return jsonify(ret)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
