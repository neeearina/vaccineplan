import django.core.exceptions
import django.utils.translation


def length(value):
    if len(value) <= 10:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                "Слишком короткий текст.",
            ),
            code="invalid_length",
        )
