import os
import json
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

DATABASE = 'results.json'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class MyForm(FlaskForm):
    name = StringField('Namn', validators=[InputRequired()])
    email = StringField('Epost', validators=[InputRequired()])
    is_cool = BooleanField('Är du cool?')
    phonenumber = DecimalField('Telefonnummer', validators=[InputRequired()])
    message = TextAreaField('Medelande', validators=[InputRequired()])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
        form = MyForm()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            is_cool = form.is_cool.data
            phonenumber = form.phonenumber.data
            message = form.message.data

            return (
               f'Namn: {name} <br>'
               f'Epost: {email} <br>'
               f'Är cool?: {is_cool} <br>'
               f'Telefonnummer: {phonenumber} <br>'
               f'Message: {message} <br>'
            )
        return render_template('survey.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
