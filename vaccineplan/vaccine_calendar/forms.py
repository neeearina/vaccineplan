import django.forms


class CalendarDateTimeForm(django.forms.Form):
    date = django.forms.DateField(
        label="Дата",
        required=True,
        widget=django.forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date"},
        ),
        input_formats=["%Y-%m-%d"],
    )
