import django.conf
import django.core.mail


def send_mail_to_clinic_admin(status, approved, recipient):
    message = (
        "Ваша заявка изменила свой статус."
        "После одобрения заявки мы отправим письмо на эту почту."
    )
    if status == "OK" and approved:
        message = (
            "Ваша заявка была рассматрена и одобрена."
            "Для доступа зайдите в ваш личный кабинет и перейдите в раздел"
            "'Администрирование клиники'."
        )
    elif status == "OK" and not approved:
        message = "Ваша заявка была рассматрена, но не была одобрена."
    django.core.mail.send_mail(
        "Изменение статуса заявки",
        message,
        django.conf.settings.EMAIL_ADDRESS,
        [recipient],
    )
