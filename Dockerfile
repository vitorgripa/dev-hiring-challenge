FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN apt update -y

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", ":8000", "core.wsgi"]