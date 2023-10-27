FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

COPY requirements.txt /backend
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /backend/app

EXPOSE 8000

CMD ["python", "app/main.py"]