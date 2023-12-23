# VaccinePlan

![Главная страница](https://github.com/neeearina/vaccineplan/raw/main/pagescreen/mainpage.png)

![Болезни на главной странице](https://github.com/neeearina/vaccineplan/raw/main/pagescreen/illnesses.png)

## Платформа для планирования вакцинации. Это избавит вас от лишних звонков и очередей в регистратуру.

## На сайте вы можете:

* Зарегистрировать личный аккаунт
* Просмотреть поликлиники и имеющиеся вакцины в ней
* Прикрепиться к определенной поликлинике
* Просмотреть и составить личный календарь вакцинации
* Подать заявление на администрирование клиники

# Инструкция по запуску проекта

## Основные настройки

### Склонируйте репозиторий с помощью git команды:

```
git clone https://github.com/neeearina/vaccineplan.git
```

### Создайте виртуальное окружение и активируйте его:

```
python3 -m venv venv 
```

```
source venv/bin/activate 
```

### Зависимости проекта

Установить зависимости для прод режима:

```
pip3 install -r requirements/prod.txt
```

для дев режима (включает в себя установку продовых зависимостей):

```
pip3 install -r requirements/dev.txt
```

для тестов:

```
pip3 install -r requirements/test.txt
```

### Переменные виртуального окружения

Создайте в корнейвой директории проекта файл .env. Заполните файл переменными
окружения по примеру файла `.example_env`, расположенный также в корневой
директории проекта.

Значение переменной DJANGO_DEBUG в прод режиме False, в дев режиме True. От
этого значения зависит отображение данных на страницах.

# Все дальнейшие команды выполняются из директории team5/vaccineplan

### Секретный ключ

Получить данные секретного ключа для проекта можно с помощью выполнения
следующих команд в терминале:

```
python3 manage.py shell
```

```
from django.core.management.utils import get_random_secret_key
```

```
get_random_secret_key()
```

## Последующие команды выполняются из директории проекта `vaccineplan`

### Выполните миграции для создания таблиц в БД:

```
python3 manage.py migrate
```

### Актуальная ER диаграмма со структурой БД по ссылке

[ERD](https://dbdiagram.io/d/VaccinePlan-65733c7756d8064ca0a99943)

### Загрузите фикстуры в БД:

```
python3 manage.py loaddata fixtures/cities.json
```

```
python3 manage.py loaddata fixtures/illnesses.json
```

```
python3 manage.py loaddata fixtures/vaccines.json
```

### Создайте пользователя для входа в admin-панель:

```
python3 manage.py createsuperuser
```

После выполнения команды заполните все нужные поля в консоли (юзернейм, почта,
пароль и т.д.)

### Запустите проект с помощью следующей команды и перейдите по ссылке в терминале:

```
python3 manage.py runserver
```
