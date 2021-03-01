from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
	file = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])  ])
