[![Pipeline Status](https://gitlab.crja72.ru/django_2023/students/163338-maks060109-47231/badges/main/pipeline.svg)]

# django-spec-1

## Инструкция по запуску проекта:

#### Клонирование репозитория

- Клонируйте репозиторий перед началом работыы

```bash
git clone <url репозитория>
```

#### Создание и активация *venv*

- Перед работой необходимо создать и активировать виртуальное окружение
  следующими командами:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Локальный запуск

- Перейти в директорию проекта и запустить его

```bash
cd vaccineplan
```

```bash
python3 manage.py runserver
```

#### Использование .env

- Для работы необходимо заполнить переменные окружения в файле *.env*.
- В качестве примера можно использовать файл *.env.example*
- *булевые переменные могут принимать значения: ```true```, ```t```, ```y```
  , ```yes```, ```1``` в качестве **True***
- ```DJANGO_DEBUG``` - булевая переменная, переключатель дебаг мода
- В случае указания ```DJANGO_DEBUG = False``` не забудьте указать разрешенные
  хосты в качестве списка.
- ```DJANGO_ALLOWED_HOSTS``` - список хостов, разделенных через символ
  запятой (без пробела)```,```
  ```DJANGO_MAIL``` - переменная, в которой задается почта, с которой
  отправляются сообщения в фидбеке
  ```DEFAULT_USER_IS_ACTIVE``` - булевая переменная, которая задает поведение
  пользователя после регистрации. Если ***True***, то пользователь становится
  активным сразу. Иначе ему нужно проходить верификацию по почте. По умолчанию
  False, но True при включенном Debug

#### Зависимости проекта

- Для запуска проекта в dev-режиме: *requirements/dev.txt*

 ```bash
 pip install -r requirements/dev.txt
 ```

- Для тестирования проекта: *requirements/test.txt*

 ```bash
 pip install -r requirements/test.txt
 ```

- Для уcтановки основных зависимостей: *requirements/prod.txt*

 ```bash
 pip install -r requirements/prod.txt
 ```

### Структура БД

[ERD](https://app.quickdatabasediagrams.com/#/d/v9GmVc)

#### Миграции базы данных

- Для установки миграций используйте:

 ```bash
 cd vaccineplan
 python3 manage.py migrate
 ```

- Если вы внесли изменения в структуру базы данных, то сделайте новую миграцию:

 ```bash
 cd vaccineplan
 python3 manage.py makemigrations
 ```

## Настройка переводов

- Для настройки переводов на определенный язык необходимо выполнить следующую
  очередность действий:

1. В файле `settings.py` в переменную `LANGUAGES` добавить кортеж
   вида `("<код языка>", _("<название языка (на языке, укзанном в LANGUAGE_CODE)>")),`
2. Убедиться, что существует файл `locale` в корне проекта или в одном из
   приложений
3. Создать файл `.po` с переводами следующей командой (находясь в директории с
   файлом `manage.py`)

 ```bash
 django-admin makemessages -a
 ```

4. В файле `locale/<код языка>/LC_MESSAGES/django.po` отредактировать перевод
   фраз
5. Скомпиллировать переводы следующей командой:

 ```bash
 django-admin compilemessages --ignore=venv
 ```

(В директории venv также содержатся файлы .po, которые могут помешать нам. Их
следует игнорировать)

## Диаграмма базы данных

Позже

## Copyrights

- иконка сайта: itim2101, flaticon.com
