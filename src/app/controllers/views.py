from flask import Flask, request, jsonify
from app import app, db
from app.models.tables import User, Profile, Post

@app.route('/register', methods=['GET'])
#crud de user
def get_user():
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
    
        


@app.route('/register', methods=['POST'])
def create_user():
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


#Crud de profile
@app.route('/profile', methods=['GET'])
def get_profile():
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
    
        
@app.route('/profile', methods=['POST'])
def create_profile():
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


#Crud de Posts
@app.route('/post', methods=['GET'])
def get_post():
    if request.method == 'GET':
        posts = []
        postRes = Post.query.all()
        for ps in postRes:
            post = {
                'id': ps.id,
                'legend': ps.legend,
                'post_date': ps.post_date,
                'profile_id': ps.profile_id,
            }
            posts.append(posts)
       
        return jsonify({'posts': posts})
    
        


@app.route('/post', methods=['POST'])
def create_post():
    post = {
        'legend': request.json['legend'],
        'post_date': request.json['post_date'],
        'profile_id': request.json['profile_id'],
    }
    legend = post['legend']
    post_date = post['post_date']
    profile_id = post['profile_id']
    #print('UserName {}'.format(username))
    p = Post(legend, post_date, profile_id)

    db.session.add(p)
    db.session.commit()

    return jsonify({'post': post}), 201