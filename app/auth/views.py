from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data, 
							enumber=form.enumber.data,
							password=form.password.data)

		#add employee to database
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered as an employee! You may now login.')

		#redirect to the login page
		return redirect(url_for('auth.login'))

	return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		employee=Employee.query.filter_by(enumber=form.enumber.data).first()
		if employee is not None and employee.verify_password(form.password.data):
			login_user(employee)

			if employee.is_admin:
				return redirect(url_for('home.admin_dashboard'))
			else:
				return redirect(url_for('home.dashboard'))

		else:
			flash('Invalid enumber or password.')


	return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully been logged out.')

	return redirect(url_for('auth.login'))
