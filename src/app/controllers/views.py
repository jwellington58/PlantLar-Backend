from flask import Flask, request, jsonify
from app import app, db
from app.models.tables import User, Profile

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
                'id': us.id,
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


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        profiles = []
        profileRes = Profile.query.all()
        for pf in profileRes:
            profile = {
                'id': pf.id,
                'name': pf.name,
                'user_id': pf.user_id,
            }
            profiles.append(profile)
       
        return jsonify({'profiles': profiles})
    else:
        profile = {
            'name': request.json['name'],
            'user_id': request.json['user_id']
        }
        name = profile['name']
        user_id = profile['user_id']
        #print('UserName {}'.format(username))
        p = Profile(name, user_id)

        db.session.add(p)
        db.session.commit()

        return jsonify({'profile': profile}), 201