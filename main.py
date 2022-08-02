# import flask

# from unicodedata import name
from flask import Flask, render_template, request
import joblib

model = joblib.load('predict_79.pkl')

# initilaise the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



# @app.route('/dsa')
# def dsa():
#     return render_template('dsa.html')

@app.route('/formsdiabitic')
def formsdiabitic():
    return render_template('formsdiabitic.html')

@app.route('/predict', methods=['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
   

    data = model.predict([[preg , plas, pres, skin, test, mass, pedi, age]])
    if data[0] == 0:
        resp = 'not diabitic'
    else:
        resp = 'diabitic'

    return render_template('formsdibitic.html', data = resp)
    # return resp
    

    # print(number)
    # print(mail)
    # print(name)
    # return 'forms submitted'

# running the app, this should be always at the end
app.run(debug=True)


