FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt   
EXPOSE 8000
CMD  python3 manage.py runserver 
