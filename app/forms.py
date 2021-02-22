from flask_wtf.csrf import CSRFProtect

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, TextAreaField, TextField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ContactForm(FlaskForm):
    #csrf = CSRFProtect(app)
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    subject = TextField('Subject', validators=[DataRequired()])
    messageBody = TextAreaField('MessageBody', validators=[DataRequired()])

