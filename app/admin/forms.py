from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Airplane_Models, Airplane

class AirplaneForm(FlaskForm):
	"""
	for admin to add airplanes
	"""
	reg_no= IntegerField('Reg_No', validators=[DataRequired()])
	models = QuerySelectField(query_factory=lambda: Airplane_Models.query.all(), get_label="number")
	submit = SubmitField('Submit')


class AirplaneModelForm(FlaskForm):
	number = StringField('Model_No', validators=[DataRequired()])
	capacity = IntegerField('Capacity', validators=[DataRequired()])
	weight = IntegerField('Weight', validators=[DataRequired()])
	submit = SubmitField('Submit')

class TechnicianForm(FlaskForm):

	tnumber=IntegerField('Tnumber', validators=[DataRequired()])
	name= StringField('Name', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	phone_number=IntegerField('Phone Number', validators=[DataRequired()])
	salary=IntegerField('Salary', validators=[DataRequired()])
	models = QuerySelectField(query_factory=lambda: Airplane_Models.query.all(), get_label="number")
	submit=SubmitField('Submit')

class TrafficControllerForm(FlaskForm):
	exam_date=DateField('Exam Date', format='%Y-%m-%d', validators=[DataRequired()])
	submit=SubmitField('Submit')

class PlaneTestForm(FlaskForm):
    KAA_no=IntegerField('KAA_number', validators=[DataRequired()])
    name=StringField('Name', validators=[DataRequired()])
    max_score=IntegerField('Max_Score', validators=[DataRequired()])
    submit=SubmitField('Submit')

class TestInfoForm(FlaskForm):

    date=DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    hours=IntegerField('Hours', validators=[DataRequired()])
    score=IntegerField('Score',validators=[DataRequired()])
    airplanes = QuerySelectField(query_factory=lambda: Airplane.query.all(), get_label="reg_no")

    submit=SubmitField('Submit')
