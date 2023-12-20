import json
import os
import pathlib

import django
import django.conf


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vaccineplan.settings")
django.setup()


import users.models


def parse_russian_cities():
    with (
        pathlib.Path("core/russian-cities.json")
        .open(mode="r", encoding="utf-8")
    ) as file:
        data = json.load(file)

    cities = []
    for city in data:
        cities.append(city["name"])

    for city_name in cities:
        users.models.City.objects.create(name=city_name)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vaccineplan.settings")
    django.setup()

    parse_russian_cities()
