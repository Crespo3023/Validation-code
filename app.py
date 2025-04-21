from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__)

app.secret_key=os.getenv('APY_SECRET_KEY')

class LoginForm(FlaskForm):
    
    username = StringField("Username", # definir input box para el username
        validators=[DataRequired(), Length(min=3)],
        render_kw={"placeholder": "Your name"})
    
    password = PasswordField("Password", # definir input box para el password
        validators=[DataRequired(), Length (min=6)],
        render_kw={"placeholder": "Your password"})
    

    email = EmailField("Email", # definir input box para el email
        validators=[DataRequired(),],
        render_kw={"placeholder": "Your email example@gmail.com "})
    
    
    submit = SubmitField("Login",  # definir el botón de submit
        render_kw={"class": "btn btn-primary"}) # aplicar clases de CSS
    
    



@app.route("/", methods=["GET"])
def index():
    return login() # Llamar a la función login() en la dirección http://127.0.0.1:5000

@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm() # Definir las reglas de validación

    if form.validate_on_submit(): # Validar los datos entrados contra las reglas
        message = f"Usuario: {form.username.data}"
        return render_template("home.html", message=message)
    
    return render_template("index.html.jinja2", form=form)

if __name__ == "__main__":
    app.run(debug=True)