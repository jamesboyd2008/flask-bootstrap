from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField,\
    SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    # Dropdowns
    x_pol = SelectField(label='X Pol Parameters', choices=[('a', 'apes'), ('b', 'bananas'), ('c', 'crabs')])
    y_pol = SelectField(label='Y Pol Parameters', choices=[('a', 'apes'), ('b', 'bananas'), ('c', 'crabs')])
    gen_sys = SelectField(label='General System Parameters', choices=[('a', 'apes'), ('b', 'bananas'), ('c', 'crabs')])

    # datetimepicker http://eonasdan.github.io/bootstrap-datetimepicker/
    begin = DateField(id='begin_dtpicker', label='Begin:')
    end = DateField(id='end_dtpicker', label='End:')

    # Search button
    submit_button = SubmitField('Search')

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # This should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = SearchForm()
        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
