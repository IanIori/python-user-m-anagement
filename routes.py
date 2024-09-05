from flask import Blueprint, render_template
from controllers.user import add_user_function, edit_user_function
from models.user import User
import sys

main = Blueprint('main',__name__) #route name = main

@main.route('/', methods=['GET'])
def home():
        data = User.get_all()
        return render_template('index.html', data = data)

@main.route('/adduser', methods = ['GET','POST'])
def add_user():
        data = add_user_function()
        print(data,file=sys.stderr)
        return render_template('adduser.html', data = data)

@main.route('/edituser/<int:id>', methods = ['GET','POST'])
def edit_user(id):
        user = User.get_by_id(id)
        data = edit_user_function(user)
        
        return render_template('edituser.html', user=user, data=data)