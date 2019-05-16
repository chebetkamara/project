from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import AirplaneForm, AirplaneModelForm, TechnicianForm, TrafficControllerForm, PlaneTestForm, TestInfoForm
from .. import db
from ..models import Airplane, Airplane_Models, Technician, Traffic_Controller, Plane_Test, Test_Info

def check_admin():
	"""
	Prevent non-users
	"""
	if not current_user.is_admin:
		abort(403)

@admin.route('/airplanes', methods=['GET', 'POST'])
@login_required
def list_airplanes():
	"""
	List all airplanes
	"""
	check_admin()

	airplanes = Airplane.query.all()

	return render_template('/admin/airplanes/airplanes.html', airplanes=airplanes, title="Airplanes")


@admin.route('/airplanes/add', methods=['GET','POST'])
@login_required
def add_airplane():
	check_admin()
	add_airplane = True

	form=AirplaneForm()
	if form.validate_on_submit():
		airplane = Airplane(reg_no=form.reg_no.data)

		try:
			db.session.add(airplane)
			db.session.commit()
			flash('You have successfully added an airplane')

		except:
			flash('Error: airplane reg_no already exists')


	return render_template('admin/airplanes/airplane.html', action="Add",
							add_airplane=add_airplane, form=form, title="Add Airplane")


@admin.route('/airplanes/edit/<int:reg_no>', methods=['GET', 'POST'])
@login_required
def edit_airplane(reg_no):
	check_admin()

	add_airplane=False

	airplane = Airplane.query.get_or_404(reg_no)
	form = AirplaneForm(obj=airplane)
	if form.validate_on_submit():
		airplane.reg_no=form.reg_no.data
		db.session.commit()
		flash('You have successfully edited the airplanes')

		return redirect(url_for('admin.list_airplanes'))

	form.reg_no.data=airplane.reg_no
	return render_template('admin/airplanes/airplane.html', action="Edit", add_airplane=add_airplane, form=form, airplane=airplane, title="Edit airplanes")

@admin.route('/airplanes/delete/<int:reg_no>', methods=['GET', 'POST'])
@login_required
def delete_airplane(reg_no):
	check_admin()

	airplane = Airplane.query.get_or_404(reg_no)
	db.session.delete(airplane)
	db.session.commit()
	flash('You have successfully deleted the airplane')

	return redirect(url_for('admin.list_airplanes'))

	return render_template(title="Delete Airplane")


@admin.route('/airplane_models')
@login_required
def list_airplanemodels():
	check_admin()
	"""
	List all airplane models
	"""

	models = Airplane_Models.query.all()
	return render_template('admin/airplane_models/airplane_models.html', models=models, title="Airplane Models")

@admin.route('airplane_models/add', methods = ['GET', 'POST'])
@login_required	
def add_airplanemodel():

	check_admin()

	add_airplanemodel= True

	form = AirplaneModelForm()
	if form.validate_on_submit():
		airplanemodel = Airplane_Models(number=form.number.data, capacity=form.capacity.data, weight=form.weight.data)

		try:
			db.session.add(airplanemodels)
			db.session.commit()
			flash('You have successfully added a new airplane model')

		except:
			flash('Error: airplane model already exists')

		return redirect(url_for('admin.list_airplanemodels'))

	return render_template('admin/airplane_models/airplane_model.html', add_airplanemodel=add_airplanemodel, form=form, title='Add airplane model')


@admin.route('/airplane_models/edit/<string:number>', methods=['GET', 'POST'])
@login_required
def edit_airplanemodel(number):
	check_admin()

	add_airplanemodel= False

	airplanemodels = Airplane_Models.query.get_or_404(number)
	form = AirplaneModelForm(obj=airplanemodels)
	if form.validate_on_submit():
		airplanemodels.number=form.number.data
		airplanemodels.capacity=form.capacity.data
		airplanemodels.weight=form.weight.data
		db.session.add(airplanemodels)
		db.session.commit()
		flash('You have successfully edited the airplane models')

		return redirect(url_for('admin.list_airplanemodels'))


	form.number.data=airplanemodels.number
	form.capacity.data=airplanemodels.capacity
	form.weight.data=airplanemodels.weight
	return render_template('admin/airplane_models/airplane_model.html',add_airplanemodel=add_airplanemodel, form=form, Title="Edit airplane models")


@admin.route('/airplane_models/delete/<string:number>', methods=['GET', 'POST'])
@login_required
def delete_airplanemodel(number):
	check_admin()

	airplanemodels = Airplane_Models.query.get_or_404(number)
	db.session.delete(airplanemodels)
	db.session.commit()
	flash('You have successfully deleted the airplane model')

	return redirect(url_for('admin.list_airplanemodels'))

	return render_template(title="Delete airplane model")


#Technicians views

@admin.route('/technicians', methods=['GET', 'POST'])
@login_required
def list_technicians():
	check_admin()

	technicians = Technician.query.all()

	return render_template('admin/technicians/technicians.html', technicians=technicians, title="Technicians")


@admin.route('/technicians/add', methods=['GET', 'POST'])
@login_required
def add_technician():
	check_admin()

	add_technician= True
	form = TechnicianForm()
	if form.validate_on_submit():
		technician = Technician(tnumber=form.tnumber.data, name=form.name.data,address=form.address.data, phone_number=form.phone_number.data, salary=form.salary.data)
		try:
			db.session.add(technician)
			db.session.commit()
			flash('You have successfully added a technician')
		except:
			flash('Error: technician already exists')

		return redirect(url_for('admin.list_technicians'))

	return render_template('admin/technicians/technician.html', action="Add", add_technician=add_technician, form=form, title="Add Technician")

@admin.route('technicians/edit/<int:tnumber>', methods=['GET', 'POST'])
@login_required
def edit_technician(tnumber):
	check_admin()

	add_technician = False

	technician = Technician.query.get_or_404(tnumber)
	form = TechnicianForm(obj=technician)
	if form.validate_on_submit():
		technician.tnumber=form.tnumber.data
		technician.name=form.name.data
		technician.address=form.address.data
		technician.phone_number=form.phone_number.data
		technician.salary=form.salary.data
		db.session.commit()
		flash('You have successfully edited the technicians')

		return redirect(url_for('admin.list_technicians'))

	form.tnumber.data=technician.tnumber
	form.name.data=technician.name
	form.address.data=technician.address
	form.phone_number.data=technician.phone_number
	form.salary.data=technician.salary

	return render_template('admin/technicians/technician.html', action="Edit", add_technician=add_technician, form=form, technician=technician, title="Edit Technicians")


@admin.route('technicians/delete/<int:tnumber>', methods=['GET', 'POST'])
@login_required
def delete_technician(tnumber):
	check_admin()

	technician = Technician.query.get_or_404(tnumber)
	db.session.delete(technician)
	db.session.commit()
	flash('You have successfully deleted the technician.')

	return redirect(url_for('admin.list_technicians'))

	return render_template(title="Delete Technician")

# traffic controllers


@admin.route('/trafficcontrollers', methods=['GET', 'POST'])
@login_required
def list_trafficcontrollers():

	check_admin()

	trafficcontrollers= Traffic_Controller.query.all()

	return render_template('admin/trafficcontrollers/trafficcontrollers.html', trafficcontrollers=trafficcontrollers, title="Traffic Controllers")


@admin.route('/trafficcontrollers/add', methods=['GET', 'POST'])
@login_required
def add_trafficcontroller():

	check_admin()

	add_trafficcontroller= True

	form=TrafficControllerForm()

	if form.validate_on_submit():
		trafficcontroller = Traffic_Controller(exam_date=form.exam_date.data)

		try:
			db.session.add(trafficcontroller)
			db.session.commit()
			flash('You have successfully added a traffic controller')

		except:
			flash('Error: traffic controller already exists')

		return redirect(url_for('admin.list_trafficcontrollers'))

	return render_template('admin/trafficcontrollers/trafficcontrollers.html', action="Add", add_trafficcontroller=add_trafficcontroller, form=form, title="Add Traffic Controller")



#plane test views
@admin.route('/planetests', methods=['GET', 'POST'])
@login_required
def list_planetests():
	check_admin()

	planetests = Plane_Test.query.all()

	return render_template('/admin/planetests/planetests.html', planetests=planetests, title="Plane Tests")

@admin.route('planetests/add', methods=['GET', 'POST'])
@login_required 
def add_planetest():

	check_admin()

	add_planetest = True

	form = PlaneTestForm()
	if form.validate_on_submit():
		planetest = Plane_Test(KAA_no=form.KAA_no.data, name=form.name.data, max_score=form.max_score.data)

		try:
			db.session.add(planetest)
			db.session.commit()
			flash('You have successfully added a new plane test')

		except:
			flash('Error: plane test already exists')

		return redirect(url_for('admin.list_planetests'))

	return render_template('admin/planetests/planetest.html', action="Add", add_planetest=add_planetest, form=form, title="Add Plane Test")


@admin.route('planetests/edit/<int:KAA_no>', methods=['GET', 'POST'])
@login_required
def edit_planetest(KAA_no):

	check_admin()

	add_planetest=False

	planetest=Plane_Test.query.get_or_404(KAA_no)
	form = PlaneTestForm(obj=planetest)
	if form.validate_on_submit():
		planetest.KAA_no=form.KAA_no.data
		planetest.name=form.name.data
		planetest.max_score=form.max_score.data
		db.session.commit()
		flash('You have successfully edited the plane tests')

		return redirect(url_for('admin.list_planetests'))

	form.KAA_no.data=planetest.KAA_no
	form.name.data=planetest.name
	form.max_score.data=planetest.max_score

	return render_template('admin/planetests/planetest.html', action="Edit", add_planetest=add_planetest, form=form, planetest=planetest, title="Edit Plane Test")


@admin.route('planetests/delete/<int:KAA_no>', methods=['GET', 'POST'])
@login_required
def delete_planetest(KAA_no):
	check_admin()

	planetest= Plane_Test.query.get_or_404(KAA_no)
	db.session.delete(planetest)
	db.session.commit()
	flash('You have successfully deleted the plane test')

	return redirect(url_for('admin.list_planetests'))

	return render_template(title="Delete Plane Test")

#test info views
@admin.route('/testinfo', methods=['GET', 'POST'])
@login_required
def list_testinfo():

	check_admin()

	testinfo = Test_Info.query.all()

	return render_template('admin/testinfo/testinfos.html', testinfo=testinfo, title= "Test Information")

@admin.route('/testinfo/add', methods=['GET', 'POST'])
@login_required
def add_testinfo():

	check_admin()

	add_testinfo= True

	form = TestInfoForm()
	if form.validate_on_submit():
		testinfo = Test_Info(date=form.date.data, hours=form.hours.data, score=form.score.data)

		try:
			db.session.add(testinfo)
			db.session.commit()
			flash('You have successfully added test information')
		except:
			flash('Error: test information already exists')

		return redirect(url_for('admin.list_testinfo'))

	return render_template('admin/testinfo/testinfo.html', action="Add", add_testinfo=add_testinfo, form=form, title="Add Test Information")


@admin.route('/testinfo/edit/<int:hours>', methods=['GET', 'POST'])
@login_required
def edit_testinfo(hours):

	check_admin()
	add_testinfo=False

	testinfo = Test_Info.query.get_or_404(hours)
	form = TestInfoForm
	if form.validate_on_submit():
		testinfo.date= form.date.data
		testinfo.hours=form.hours.data
		testinfo.score=form.score.data
		db.session.commit()
		flash('You have successfully edited the test information')

		return redirect(url_for('admin.list_testinfo'))

	form.date.data=testinfo.date
	form.hours.data=testinfo.hours
	form.score.data=testinfo.score
	return render_template('admin/testinfo/testinfo.html', action="Edit", add_testinfo=add_testinfo, form=form, testinfo=testinfo, title="Edit Test Information")

@admin.route('/testinfo/delete/<int:hours>', methods=['GET', 'POST'])
@login_required
def delete_testinfo(hours):

	check_admin()

	testinfo= Test_Info.query.get_or_404(hours)
	db.session.delete(testinfo)
	db.session.commit()
	flash("You have successfully deleted the test information")

	return redirect(url_for('admin.list_testinfo'))

	return render_template(title="Delete Test Information")
	
