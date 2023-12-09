import django.db.utils
import django.test

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
