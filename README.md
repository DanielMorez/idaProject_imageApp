# Начало работы
<br>
Скачайте проект, перейдите в его корень и активируйте виртуальное окружение 
командой:
<br>

``$ source venv\bin\activate # for Ubuntu or Debian ``

``venv\bin\activate # for Windows ``

Если по какой-то причине, вы не можете активировать venv, попробуйте создать 
виртуальное окружение.

### Установка виртуального окружения для Windows

Через консоль перейдите в корень проекта и создайте своё виртуальное окружение этой командой
<br>
````
python3 -m venv venv 
venv\Scripts\activate.bat # Активировать venv
pip install -r requirements.txt # Установка необходимых библиотек из requirements.txt
````

## Запуск приложения

### 1. Проведите миграцию

````
$ python3 manage.py makemigrations
$ python3 manage.py migrate
````
### 2. Запустите приложение на локальной машине

````
$ python3 manage.py runserver
````

#
