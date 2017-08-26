from flask_wtf import Form, RecaptchaField
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import InputRequired, Length


class LoginForm(Form):
    username = TextField(
        "Username",
        validators=[
            InputRequired(message="Need an name"),
            Length(max=50)
        ]
    )
    password = TextField(
        "Password",
        validators=[
            InputRequired(message="Need a password"),
            Length(max=50)
        ]
    )
    recaptcha = RecaptchaField("Copy the words appearing below")
    submit = SubmitField("Login")


class PostForm(Form):
    title = TextField("Title")
    postname = TextField("Postname")
    content = TextAreaField("Postname")
    tags = TextField("Tags")
    # {% for category in g.categories %}
    # {{ category.category_name }}<input type="radio" name="category" value="{{ category.id }}" />&nbsp;&nbsp;
    # {% endfor %}
    recaptcha = RecaptchaField("Copy the words appearing below")
    submit = SubmitField("Submit")


class EForm(Form):
    postnumber = TextField("Postnumber")
    submit = SubmitField("Submit")
