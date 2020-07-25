from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def first():
    return 'Hello'


@app.route('/todos', methods=['GET'])
def getTodos():
    todos = [
        {
            'title': 'wake up early',
            'completed': False
        },
        {
            'title': 'buy mask',
            'completed': True
        }
    ]
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def addTodo():
    return 'added'


if __name__ == "__main__":        # on running python app.py
    app.run(host = '0.0.0.0', port=5000, debug=True)