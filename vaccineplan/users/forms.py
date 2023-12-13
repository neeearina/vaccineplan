import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms
import django.forms.fields

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
        ]


class ProfileForm(django.forms.Form):
    class Meta:
        model = users.models.CustomUser
        fields = [
            users.models.CustomUser.first_name.field.name,
            users.models.CustomUser.last_name.field.name,
            users.models.CustomUser.middle_name.field.name,
            users.models.CustomUser,
        ]
