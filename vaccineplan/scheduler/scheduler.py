import apscheduler.schedulers.background
import django.utils
import django_apscheduler.jobstores

import vaccine_calendar.models


def send_notifications():
    today = django.utils.timezone.now()
    soon_records = vaccine_calendar.models


def start():
    scheduler = apscheduler.schedulers.background.BackgroundScheduler()
    scheduler.add_jobstore(
        django_apscheduler.jobstores.DjangoJobStore(),
        "default",
    )
    # run this job every 24 hours
    scheduler.add_job(
        deactivate_expired_accounts,
        "interval", hours=24,
        name="clean_accounts",
        jobstore="default",
    )
    django_apscheduler.jobstores.register_events(scheduler)
    scheduler.start()
