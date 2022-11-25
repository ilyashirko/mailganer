# E-mail service
E-mail service for mass sending emails using `gmail` host.  
You need `python 2.7`, `poetry 1.1.15` and `virtualenv 20.15.1` to work with service.
## Installation
clone repo, enter root dir:
```sh
git clone https://github.com/ilyashirko/mailganer && cd mailganer
```
Create virtual environment, activate and install dependencies:
```sh
virtualenv --python=python2.7 mailganer_env &&
source mailganer_env/bin/activate &&
poetry install
```
now its time to create `.env` file, you can edit `.env.example` and then rename it with `.env`.  
You need:  
- `DJANGO_SECRET_KEY` - you can generate it [here](https://djecrety.ir/)
- `EMAIL_HOST_USER` (required) - your [business account](https://www.gmail.com)
- `EMAIL_HOST_PASSWORD`(required) - [password for application](https://support.google.com/accounts/answer/185833?hl=ru)

- `DEBUG` (optional) - 1 if you need debug mode (default - `False`)
- `ALLOWED_HOSTS` (optional) - your hosts (default - `127.0.0.1`)
- `EMAIL_HOST` (optional) - host of your email service (default - `smtp.gmail.com`)
- `EMAIL_PORT` (optional) - port (default - `465` for ssl connection)
- `EMAIL_USE_SSL` (optional) - `0` if you want to use TSL (default - `1`)
- `EMAIL_USE_TSL` (optional) - `1` if you want to use SSL (default - `0`)
After creating `.env` you can finish setup of django application and create superuser:
```sh
python manage.py migrate && python manage.py createsuperuser
```
## Usage
For using app you should launch django app, celery worker and redis-server:
```sh
redis-server && python manage.py runserver | python -m celery -A mailganer worker -l info
```
now you can enter django admin `{your_host}/admin` using superuser login and password.  
To make your first distribution you should:
- create Subscriber objects - people who will take your letters.
- create template in html format. You can use `firstname`, `lastname`, `birthday` and `email` of your subscribers. This data will add automaticaly (example below).
- create message object.
- select message and choose `send message` option.
### Template example
```
<div style="font-family: 'Droid Sans Mono', 'monospace', monospace; font-size: 14px; line-height: 19px; white-space: pre;">
    <div>Вас зовут: {{ firstname }} {{ lastname }}.</div>
    <div>Ваш день рождения: {{ birthday }}.</div>
    <br />
    <div>Ваша почта: {{ email }}</div>
<img src="{{ open_pixel_url }}" width="1px" height="1px" border="0"/>
</div>
```
`<img src="{{ open_pixel_url }}" width="1px" height="1px" border="0"/>` - pixel for open letter report