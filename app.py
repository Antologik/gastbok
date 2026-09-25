import os
import json
from datetime import datetime
from flask import Flask, render_template, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

APPEND_FILE = 'results.json'


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

            with open(APPEND_FILE, 'r') as file:
                json_contents = json.load(file)

            with open(APPEND_FILE, 'w', encoding='utf-8') as file:
                print(json_contents)
                is_cool = str(is_cool).lower()
                str_response = f'{{"Date": "{datetime.now()}", "Name": "{name}", "Email": "{email}", "Is cool": {is_cool}, "Phonenumber": {phonenumber}, "Message": "{message}"}}'
                print(str(str_response))
                print(str_response)
                # str_response = '{"name": "Sigma", "age": 1}'
                dict_response = json.loads(str(str_response))
                json_contents.get("respondents").append(dict_response)
                print(json_contents)
                print(str(json_contents))
                file.write(str(json_contents))

            with open(APPEND_FILE, 'r', encoding='utf-8') as f:
                content = f.read()


            return (render_template('form-complete.html'))
        return render_template('survey.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
