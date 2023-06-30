from . import db #means I can access any .py or can sau from website ...
from flask_login import UserMixin 
from sqlalchemy.sql import func 

class Note(db.Model) :
    # automatically create a unique ID 
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # data = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_id in each Note --> reference to parent --> (user) 
    # we can figure out which user create it 
    # user.id --> get from class User but being represented
    # .id is given from an attribute of class User
 
# UserMixin ??? inherit from it ??? 
class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') 
    # a list
    # Note need capital referencing class Note
    # this code just show you relationship one-many which is commmon
    # look up another type : one-one, many-one
