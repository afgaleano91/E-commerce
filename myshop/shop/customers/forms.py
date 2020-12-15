from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register




class CustomerRegisterForm(FlaskForm):
    name = StringField('Nombre: ')
    username = StringField('Usuario: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Contraseña: ', [validators.DataRequired(), validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('Repetir contraseña: ', [validators.DataRequired()])
    country = StringField('Pais: ', [validators.DataRequired()])
    city = StringField('Ciudad: ', [validators.DataRequired()])
    contact = StringField('Celular: ', [validators.DataRequired()])
    address = StringField('Dirección: ', [validators.DataRequired()])
    zipcode = StringField('Código Postal: ', [validators.DataRequired()])

    profile = FileField('Perfil', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Solo imagenes por favor')])
    submit = SubmitField('Registro')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Este nombre de usuario ya esta en uso!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("Este email ya esta en uso!")

    


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Contraseña: ', [validators.DataRequired()])

   




   

 

    

     

   


    

