from flask import Flask, request, jsonify
from app import app, db
from app.models.tables import User

# users = [
#     {

#     }
# ]

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        users = []
        userRes = User.query.all()
        for us in userRes:
            user = {
                'username': us.username,
                'password': us.password,
            }
            users.append(user)
       
        return jsonify({'users': users})
    else:
        user = {
            'username': request.json['username'],
            'password': request.json['password']
        }
        username = user['username']
        password = user['password']
        #print('UserName {}'.format(username))
        u = User(username, password)

        db.session.add(u)
        db.session.commit()

        return jsonify({'user': user}), 201