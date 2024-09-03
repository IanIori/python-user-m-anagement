from flask import Blueprint, render_template

main = Blueprint('main',__name__) #route name = main

@main.route('/', methods=['GET'])
def home():
        return render_template('index.html')

@main.route('/adduser', methods = ['GEST','POST'])
def add_user():
        return render_template('adduser.html')