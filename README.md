# Пользователи Django

Минимальный Django-проект с кастомной моделью пользователя. Для локального запуска:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Откройте `/admin/` и войдите с учётной записью суперпользователя. Пользователи входят по email; роль по умолчанию — `CLIENT`.
