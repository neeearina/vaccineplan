import os
import time

import django
import selenium
import selenium.webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vaccineplan.settings")
django.setup()

import vaccines.models


class VaccineCategoriesParser:
    def __init__(self):
        self.browser = selenium.webdriver.Chrome()

    def create_category_table(self):
        try:
            self.browser.get(
                "https://asko-med.ru/blog/vaktsiny"
                "/spisok-vaktsin-v-rossii-spravochnyy-material/",
            )
            time.sleep(2)
            container = self.browser.find_element(
                selenium.webdriver.common.by.By.CLASS_NAME,
                "test-block",
            )
            illnesses_list = container.find_elements(
                selenium.webdriver.common.by.By.TAG_NAME,
                "h3",
            )
            for illness in illnesses_list:
                vaccines.models.VaccineCategories.objects.create(
                    name=illness.text,
                )
            time.sleep(1)
            self.browser.quit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobik_api.settings")
    django.setup()
    parser = VaccineCategoriesParser()
    parser.create_category_table()
