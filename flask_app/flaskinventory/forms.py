from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,NumberRange



class addproduct(FlaskForm):
    prodname = StringField('Nom du Produit', validators=[DataRequired()])
    prodqty = IntegerField('Quantité', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    prodsubmit = SubmitField('Enregistrer')

class editproduct(FlaskForm):
    editname = StringField('Nom du Produit', validators=[DataRequired()])
    editqty = IntegerField('Quantité', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    editsubmit = SubmitField('Enregistrer')

class addlocation(FlaskForm):
    locname = StringField('Nom de l\' emplacement', validators=[DataRequired()])
    locsubmit = SubmitField('Enregistrer')

class editlocation(FlaskForm):
    editlocname = StringField('Nom de l\' emplacement', validators=[DataRequired()])
    editlocsubmit = SubmitField('Enregistrer')

class moveproduct(FlaskForm):
    mprodname = SelectField(
        'Nom du Produit')
    src = SelectField(
        'Source')
    destination = SelectField(
        'Destination')
    mprodqty = IntegerField('Quantité', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    movesubmit = SubmitField('Déplacer')
class ProductSearchForm(FlaskForm):
    search_query = StringField('Rechercher un produit')
    searchsubmit = SubmitField('Rechercher')