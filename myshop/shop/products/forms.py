from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    name = StringField('Nombre', [validators.DataRequired()])
    price = FloatField('Precio', [validators.DataRequired()])
    discount = IntegerField('Descuento', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colores', [validators.DataRequired()])
    discription = TextAreaField('Descripción', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Solo imagenes por favor'])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Solo imagenes por favor'])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Solo imagenes por favor'])
