import django.contrib
import django.db.utils
import django.test

import clinics.models
import core.models
import users.models
import vaccines.models


class VaccinesTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = vaccines.models.VaccineCategories.objects.create(
            name="Тестовая болезнь 1",
        )
        cls.vaccine1 = vaccines.models.Vaccines.objects.create(
            name="Тестовая вакцина 1",
            category=cls.category1,
        )

    def test_create_vaccines(self):
        vaccines_count = vaccines.models.Vaccines.objects.all().count()
        vaccines.models.Vaccines.objects.create(
            name="Тестовая вакцина 1",
            category=self.category1,
        )
        new_vaccines_count = vaccines.models.Vaccines.objects.all().count()
        self.assertEqual(vaccines_count + 1, new_vaccines_count)

    def test_unabled_create_vaccines(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            vaccines.models.Vaccines.objects.create(
                name="Тестовая вакцина 1",
            )

    def test_relations_with_category(self):
        vaccine = vaccines.models.Vaccines.objects.get(pk=1)
        related_model = vaccine._meta.get_field("category").related_model
        self.assertEqual(related_model, vaccines.models.VaccineCategories)


class AvailabilityTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city = core.models.City.objects.create(
            name="Москва",
        )
        cls.user = users.models.CustomUser.objects.create_user(
            username="john",
            city=cls.city,
            email="jlennon@beatles.com",
            password="glass onion",
        )
        cls.category1 = vaccines.models.VaccineCategories.objects.create(
            name="Тестовая болезнь 1",
        )
        cls.vaccine1 = vaccines.models.Vaccines.objects.create(
            name="Тестовая вакцина 1",
            category=cls.category1,
        )

        cls.clinic = clinics.models.Clinics.objects.create(
            admin=cls.user,
            name="Тестовая клиника",
            city=cls.city,
            address="Морозная улица 23Б",
            lisense="Тестовая лицензия",
            phone_number="89287254326",
            clinic_mail="test@gmail.com",
        )
        vaccines.models.Availability.objects.create(
            vaccines=cls.vaccine1,
            clinic=cls.clinic,
        )

    def test_create_availability(self):
        initial_count = vaccines.models.Availability.objects.all().count()
        vaccines.models.Availability.objects.create(
            vaccines=self.vaccine1,
            clinic=self.clinic,
        )
        new_count = vaccines.models.Availability.objects.all().count()
        self.assertEqual(initial_count + 1, new_count)

    def test_relations_with_vaccines(self):
        availability = vaccines.models.Availability.objects.get(pk=1)
        related_model = availability._meta.get_field("vaccines").related_model
        self.assertEqual(related_model, vaccines.models.Vaccines)

    def test_relations_with_clinic(self):
        availability = vaccines.models.Availability.objects.get(pk=1)
        related_model = availability._meta.get_field("clinic").related_model
        self.assertEqual(related_model, clinics.models.Clinics)
