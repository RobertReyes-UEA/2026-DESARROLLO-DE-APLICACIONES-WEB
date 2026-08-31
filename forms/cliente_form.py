from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ClienteForm(FlaskForm):

    nombre = StringField(
        "Nombre completo",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(
                min=3,
                max=100,
                message="El nombre debe tener entre 3 y 100 caracteres."
            )
        ]
    )

    correo = EmailField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingrese un correo electrónico válido.")
        ]
    )

    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Length(
                min=7,
                max=15,
                message="El teléfono debe tener entre 7 y 15 caracteres."
            )
        ]
    )

    direccion = TextAreaField(
        "Dirección",
        validators=[
            DataRequired(message="La dirección es obligatoria."),
            Length(
                min=5,
                max=200,
                message="La dirección debe tener al menos 5 caracteres."
            )
        ]
    )
