from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length


class courseForm(FlaskForm):
    
    courseCode = StringField('Course Code',
                             validators=[DataRequired(), Length(max=5)])
    
    courseName = StringField('Course Name',
                             validators=[DataRequired(), Length(max=100)])
    
    referCode = StringField('Old ID',
                            validators=[DataRequired(), Length(max=5)])
    
    submit = SubmitField('Submit')