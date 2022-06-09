FROM python:3.8
 ## гарантирует, что наш вывод консоли выглядит знакомым и не буферизируется Docker, что нам не нужно
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:$PORT