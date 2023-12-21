import django.test
import django.urls
import parameterized.parameterized

import clinics.forms
import clinics.models
import core.models
import users.models


class ClinicsModelTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city = core.models.City.objects.create(
            name="Москва",
        )
        cls.user = users.models.CustomUser.objects.create_user(
            username="testadmin",
            password="Test!23@kxk",
            city=cls.city,
        )
        cls.clinic = clinics.models.Clinics.objects.create(
            admin=cls.user,
            name="клиника 1",
            city=cls.city,
            address="Ул. Садовая 117А",
            lisense="Тестовая лицензия для клиники",
            phone_number="89297340912",
            clinic_mail="clinic@gmail.com",
        )

    def test_relations_with_category(self):
        clinic = clinics.models.Clinics.objects.get(pk=1)
        related_model = clinic._meta.get_field("admin").related_model
        self.assertEqual(
            related_model,
            users.models.CustomUser,
        )


class ClinicsFormTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form = clinics.forms.ClinicsForm
        cls.city = core.models.City.objects.create(
            name="Москва",
        )

    def test_valid_data(self):
        form_data = {
            "name": "клиника 1",
            "city": self.city,
            "address": "Ул. Садовая 117А",
            "lisense": "Тестовая лицензия для клиники",
            "phone_number": "89297340912",
            "clinic_mail": "clinic@gmail.com",
        }
        form = clinics.forms.ClinicsForm(form_data)
        self.assertTrue(form.is_valid())

    @parameterized.parameterized.expand(
        [
            ["name"],
            ["address"],
            ["lisense"],
            ["phone_number"],
            ["clinic_mail"],
        ],
    )
    def test_empty_fields(self, field):
        form_data = {
            "name": "",
            "address": "",
            "lisense": "",
            "phone_number": "",
            "clinic_mail": "",
        }
        form = clinics.forms.ClinicsForm(form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field))
