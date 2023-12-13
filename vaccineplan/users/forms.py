from collections.abc import Mapping
from typing import Any
import django.contrib.auth.forms
import django.contrib.auth.models
from django.core.files.base import File
from django.db.models.base import Model
import django.forms
import django.forms.fields
from django.forms.utils import ErrorList

import users.models


__all__ = []


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    email = django.forms.EmailField(
        required=True,
    )

    class Meta:
        model = users.models.CustomUser
        fields = [
            users.models.CustomUser.username.field.name,
            users.models.CustomUser.email.field.name,
            users.models.CustomUser.first_name.field.name,
            users.models.CustomUser.last_name.field.name,
            users.models.CustomUser.middle_name.field.name,
            users.models.CustomUser.gender.field.name,
            users.models.CustomUser.birthday.field.name,
        ]


class ProfileForm(django.forms.ModelForm):
    bithday_field = django.forms.DateField(
        widget=django.forms.DateInput(
            attrs={
                "type": "date",
            },
        ),
        label="Дата рождения",
    )

    class Meta:
        model = users.models.CustomUser
        fields = [
            users.models.CustomUser.username.field.name,
            users.models.CustomUser.first_name.field.name,
            users.models.CustomUser.last_name.field.name,
            users.models.CustomUser.middle_name.field.name,
            users.models.CustomUser.image.field.name,
            users.models.CustomUser.clinic.field.name,
        ]
