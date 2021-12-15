from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class collegeForm(FlaskForm):
    
    collegeCode = StringField('College Code',
                              validators=[DataRequired(), Length(max=6)])

    collegeName = StringField('College Name',
                              validators=[DataRequired(), Length(max=100)])

    referCode = StringField('Old Code',
                            validators=[DataRequired(), Length(max=6)])

    submit = SubmitField('Submit')