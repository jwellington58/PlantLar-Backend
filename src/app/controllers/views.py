from flask import Flask, request, jsonify
from app import app, db
from app.models.tables import User

users = [
    {

    }
]

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return jsonify({'users': users})
    else:
        user = {
            'username': request.json['username'],
            'password': request.json['password']
        }
        '''username = user['username']
        password = user['password']

        u = User(username, password)

        db.session.add(u)
        db.session.commit()'''

        return jsonify({'user': user}), 201