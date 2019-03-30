from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/task-add', methods=['POST'])
def post_task():
    n_id = request.json['id']
    n_title = request.json['title']
    n_desc = request.json['description']
    n_done = request.json['done']
    tasks.append({"id": n_id, "title": n_title,"description":n_desc, "done":n_done})
    return jsonify({"message": "task added!"})

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
