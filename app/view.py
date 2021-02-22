from flask.helpers import url_for
from app import app
from flask import render_template, request, redirect

@app.route('/')
def home():
    return render_template('index.html', title = "Learn University ")

@app.route('/course')
def get_course():
    return render_template('course.html', title = "Learn University")

@app.route('/login')    
def login():
    return render_template('login.html', title="Bienvenido")

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        redirect(url_for('login'))
    return render_template('join.html')
