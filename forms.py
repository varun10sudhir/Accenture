from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,DataRequired

class TaskForm(FlaskForm):
    todo = StringField(label='Todo',validators=[DataRequired()])
    submit = SubmitField(label='Add task')


class NewCommit(FlaskForm):
    header = StringField(label='Header',validators=[DataRequired()])
    description = StringField(label='Description',validators=[DataRequired()])