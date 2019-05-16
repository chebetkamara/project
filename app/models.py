from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db,login_manager

class Employee(UserMixin, db.Model):

    __tablename__= 'employees'

    union_no = db.Column(db.Integer)
    email=db.Column(db.String(60), unique=True)
    password_hash=db.Column(db.String(128))
    enumber = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20))
    is_admin=db.Column(db.Boolean, default=False)

    def get_id(self):
        return (self.enumber)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {} {} {}'.format(self.role, self.union_no, self.enumber)


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Airplane(db.Model):

    __tablename__ = 'airplanes'

    reg_no = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), db.ForeignKey('models.number', onupdate='cascade'))

    def __repr__(self):
        return 'Airplane: {} {}'.format(self.model_number, self.name)

class Airplane_Models(db.Model):
        
    __tablename__ = 'models'
    
    number = db.Column(db.String(20), primary_key=True)
    capacity = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    planes = db.relationship('Airplane', backref = 'model', lazy = 'dynamic')
    techs= db.relationship('Technician', backref = 'work', lazy = 'dynamic')
        
    def __repr__(self):
        return 'Model: {}, capacity: {}, weight: {}'.format(self.number, self.capacity, self.weight)

class Technician(db.Model):

    __tablename__ = 'technicians'

    tnumber=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(60))
    phone_number=db.Column(db.Integer, unique=True)
    salary=db.Column(db.Integer)
    number=db.Column(db.String(20), db.ForeignKey('models.number' , onupdate='cascade'), unique=True)

    def __repr__(self):
        return  'Technician: {} {} {} {} {}'.format(self.tnumber, self.name, self.address, self.phone_number, self.number)

class Traffic_Controller(db.Model):

    __tablename__= 'traffic_controllers'

    exam_date=db.Column(db.DateTime, primary_key=True)


    def __repr__(self):
        return 'Traffic_Controller: {}'.format(self.exam_date)

class Plane_Test(db.Model):

    __tablename__ = 'planetests'
    KAA_no=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    max_score=db.Column(db.Integer)

    def __repr__(self):
        return 'Plane_test: {} {} {}'.format(self.KAA_no, self.name, self.max_score)

class Test_Info(db.Model):

    __tablename__= 'testinfo'

    date=db.Column(db.DateTime)
    hours=db.Column(db.Integer, primary_key=True)
    score=db.Column(db.Integer)
    db.reg_no=db.Column(db.Integer, db.ForeignKey('airplanes.reg_no'))

    def __repr__(self):
        return 'Test_Info: {} {} {}'.format(self.date, self.hours, self.score)