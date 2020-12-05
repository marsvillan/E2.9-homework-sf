
## Установка и запуск (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
```
$ git clone https://github.com/marsvillan/E2.9-homework-sf
$ cd E2.9-homework-sf
```
- создать виртуальное окружение
```
$ python -m venv env
```
- применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```
- установить зависимости
```
$ pip install -r requirements.txt
```
- создать структуру базы данных
```
$ python manage.py migrate
```
- создать переменные окружения для работы SendGrid
```
### Если у вас Linux:
$ export SENDGRID_API_KEY=<ключ API>
$ export SENDGRID_TEMPLATE_ID=<id шаблона письма>
$ export SENDGRID_FROM=<поле From письма>
### Если у вас Windows:
$ setx SENDGRID_API_KEY <ключ API>
$ setx SENDGRID_TEMPLATE_ID <id шаблона письма>
$ setx SENDGRID_FROM <поле From письма>
```
В шаблоне используются переменные: data.sent_datetime и data.text
- запустить сервер
```
$ python manage.py runserver
```

## Использование
http://127.0.0.1:8000/
