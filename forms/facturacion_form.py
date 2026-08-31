from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange


class FacturacionForm(FlaskForm):

    cliente = StringField(
        "Cliente",
        validators=[
            DataRequired(message="El cliente es obligatorio."),
        ]
    )

    concepto = StringField(
        "Concepto",
        validators=[
            DataRequired(message="El concepto es obligatorio.")
        ]
    )

    total = FloatField(
        "Total",
        validators=[
            DataRequired(message="El total es obligatorio."),
            NumberRange(
                min=0,
                message="El total debe ser mayor o igual a 0."
            )
        ]
    )

    estado = SelectField(
        "Estado",
        choices=[
            ("", "Seleccione un estado"),
            ("Pendiente", "Pendiente"),
            ("Pagada", "Pagada"),
            ("Anulada", "Anulada")
        ],
        validators=[
            DataRequired(message="Seleccione un estado.")
        ]
    )
