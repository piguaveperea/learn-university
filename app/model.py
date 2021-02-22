from app import db
from datetime import datetime

class User (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16), unique = True, nullable = False )
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    img_profile = db.Column(db.String(250))
    img_banner = db.Column(db.String(250))
    create_at = db.Column(db.DateTime, default = datetime.utcnow)
    post = db.relationship('Post', backref='user', lazy=True)

class Post (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable = False)
    date_post = db.Column(db.DateTime, default = datetime.utcnow )
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    commentary = db.relationship('Commentary', backref= 'post', lazy= True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'), nullable = False)
    commentary = db.relationship('Commentary', backref='course', lazy = True)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    title = db.Column(db.String(120))
    course_id = db.Column(db.Interger, db.ForeingKey('course.id'), nullable = False)
    comementary = db.relationship('Commentary', backref='leeson', lazy = True)

class Video(db.Model):
    id = db.Column(db.Integer)
    path = db.Column(db.String(250))
    lesson_id = db.Column(db.Integer, db.ForeingKey('lesson.id'), nullable = False)

class File (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String(250))

class Commentary(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'), nullable = False)

class Group(db.Model):
    pass
    