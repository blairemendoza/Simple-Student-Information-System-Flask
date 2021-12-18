from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
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
                             validators=[DataRequired(), Length(min=0)])
    
    imgFile = FileField('Photo',
                        validators=[FileAllowed('image')])
    
    referID = StringField('Old ID',
                          validators=[DataRequired(), Length(max=9)])
    
    submit = SubmitField('Submit')