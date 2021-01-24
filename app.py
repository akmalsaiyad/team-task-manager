'''
This is a TO-DO List app developed in FLASK Python

'''
from flask import Flask

from os import system
from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)




'''
pip install virtualenv
.\env\Scripts\activate.bat
pip install flask flask-sqlalchemy
'''