# Dockerfile для applicant_service
FROM python:3.9

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо залежності
COPY requirements.txt /app/

# Встановлюємо залежності
RUN pip install -r requirements.txt

# Копіюємо проект у контейнер
COPY . /app
# Виконуємо міграції та запускаємо сервер
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
