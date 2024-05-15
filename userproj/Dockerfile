FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt   
EXPOSE 9000
CMD  python3 manage.py runserver  0.0.0.0:9000
