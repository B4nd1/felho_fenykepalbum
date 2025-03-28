# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


ENV PYTHONUNBUFFERED=1


RUN python manage.py collectstatic --noinput

# Run app.py when the container launches
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "felho_fenykepalbum.wsgi:application"]
CMD ["bash", "start.sh"]