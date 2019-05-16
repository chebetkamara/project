from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
	"""
	form for users to create account
	""" 
	email = StringField('Email', validators=[DataRequired(), Email()])
	enumber = IntegerField('Enumber', validators=[DataRequired()])
	union_no= IntegerField('Union Number',validators=[DataRequired()])
	role= StringField('Role', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
	confirm_password= PasswordField('Confirm Password')
	submit = SubmitField('Register')

	def validate_enumber(self, field):
		if Employee.query.filter_by(enumber=field.data).first():
			raise ValidationError('Enumber belongs to another employee')

	def validate_email(self, field):
		if Employee.query.filter_by(email=field.data).first():
			raise ValidationError('Email is already in use.')



class LoginForm(FlaskForm):
	"""
	users to login
	"""

	email = StringField('Email', validators=[DataRequired(), Email()])
	enumber = IntegerField('Enumber', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')