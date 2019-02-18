from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

    profile = db.relationship('User', backref='user', uselist=False)

    def __init__(self, username, password, profile_id):
        self.username = username
        self.password = password
        self.profile_id = profile_id


class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    posts = db.relationship('Post', backref='post', lazy='dynamic')
    followers = db.relationship('Folower_Followed', backref='follower_followed', lazy='dynamic')
    followeds = db.relationship('Folower_Followed', backref='follower_followed', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    legend = db.Column(db.Text)
    post_date = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

    photos = db.relationship('Photo', backref='photo', lazy='dynamic')

    def __init__(self, legend, post_date, profile_id):
        self.legend = legend
        self.post_date = post_date
        self.profile_id = profile_id


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path_photo = db.Column(db.String(50))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __init__(self, path_photo, post_id):
        self.path_photo = path_photo
        self.post_id =post_id


class Folower_Followed(db.Model):
    __tablename__ = 'follower_followed'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_id_follower = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile_id_followed = db.Column(db.Integer, db.ForeignKey('profile.id'))

    def __init__(self, profile_id_follower, profile_id_followed):
        self.profile_id_follower = profile_id_follower
        self.profile_id_followed = profile_id_followed


# Criação do banco
db.create_all()