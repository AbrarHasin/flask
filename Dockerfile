FROM python:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD [ "python", "./main.py", "runserver", "0.0.0.0:8000" ]