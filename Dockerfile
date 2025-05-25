FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app
COPY media/ /app/media/


RUN pip install --upgrade pip \
&& pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
