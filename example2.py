from flask import Flask, jsonify,json,request,Response

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


def get_all_users():
    file = open('data.txt','r',encoding='utf-8')
    js = json.load(file)
    file.close()
    return jsonify(js)

def create_user():
    req_js = request.args
    file = open('data.txt','w',encoding='utf-8')
    file.write(json.dumps(req_js))
    file.close()
    return Response('{"status": "ok"}', status=200, mimetype='application/json')



@app.route('/users', methods=['GET','POST'])

def users(*args, **kwars):
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        return create_user()
    elif request.method == 'PATCH':
        return update_user()
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)