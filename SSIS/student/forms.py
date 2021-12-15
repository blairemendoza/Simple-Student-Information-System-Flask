from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class studentForm(FlaskForm):
    
    idNumber = StringField('ID Number',
                           validators=[DataRequired(), Length(max=9)])
    
    lastName = StringField('Last Name', 
                           validators=[DataRequired(), Length(max=50)])
    
    firstName = StringField('First Name', 
                            validators=[DataRequired(), Length(max=100)])
    
    yearLevel = IntegerField('Year Level',
                             validators=[DataRequired()])
    
    referID = StringField('Old ID',
                          validators=[DataRequired(), Length(max=9)])
    
    submit = SubmitField('Submit')