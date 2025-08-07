FROM python:3.11-slim

WORKDIR /app

# Копируем всё содержимое папки app внутрь контейнера
COPY ./app ./app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r ./app/requirements.txt

# Объявляем порт, который слушает uvicorn
EXPOSE 8000

# Запускаем приложение на 8000 порту
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
