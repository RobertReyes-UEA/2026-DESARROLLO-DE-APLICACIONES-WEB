from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ProveedorForm(FlaskForm):

    empresa = StringField(
        "Nombre de la empresa",
        validators=[
            DataRequired(message="El nombre de la empresa es obligatorio."),
            Length(
                min=3,
                max=100,
                message="Debe tener entre 3 y 100 caracteres."
            )
        ]
    )

    contacto = StringField(
        "Persona de contacto",
        validators=[
            DataRequired(message="El contacto es obligatorio."),
            Length(
                min=3,
                max=100,
                message="Debe tener entre 3 y 100 caracteres."
            )
        ]
    )

    correo = EmailField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingrese un correo válido.")
        ]
    )

    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Length(min=7, max=15)
        ]
    )

    direccion = TextAreaField(
        "Dirección",
        validators=[
            DataRequired(message="La dirección es obligatoria.")
        ]
    )
