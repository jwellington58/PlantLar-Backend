from flask import Flask, request, jsonify, abort
from app import app, db
from app.models.tables import User, Profile, Post, Photo

#crud de user
@app.route('/user', methods=['GET'])
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


@app.route('/user', methods=['POST'])
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


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    userRes = User.query.filter_by(id=user_id).first_or_404()
    if userRes==None:
        abort(404)
    db.session.delete(userRes)
    db.session.commit()
    return jsonify({'result': True})



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
    p = Profile(name, user_id)

    db.session.add(p)
    db.session.commit()

    return jsonify({'profile': profile}), 201


@app.route('/profile/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    p = Profile.query.filter_by(id=profile_id).first_or_404()
    if p==None:
        abort(404)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'result': True})


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
            posts.append(post)
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
    p = Post(legend, post_date, profile_id)

    db.session.add(p)
    db.session.commit()

    return jsonify({'post': post}), 201


@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    p = Post.query.filter_by(id=post_id).first_or_404()
    if p==None:
        abort(404)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'result': True})



#crud de photo
@app.route('/photo', methods=['GET'])
def get_photo():
    if request.method == 'GET':
        photos = []
        photoRes = Photo.query.all()
        for pho in photoRes:
            photo = {
                'id': pho.id,
                'path_photo': pho.path_photo,
                'post_id': pho.post_id,
            }
            photos.append(photo)
       
        return jsonify({'photos': photos})


@app.route('/photo', methods=['POST'])
def create_photo():
    photo = {
        'path_photo': request.json['path_photo'],
        'post_id': request.json['post_id']
    }
    path_photo = photo['path_photo']
    post_id = photo['post_id']
    pho = Photo(path_photo, post_id)

    db.session.add(pho)
    db.session.commit()

    return jsonify({'photo': photo}), 201


@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_photo(photo_id):
    pho = Photo.query.filter_by(id=photo_id).first_or_404()
    if pho==None:
        abort(404)
    db.session.delete(pho)
    db.session.commit()
    return jsonify({'result': True})