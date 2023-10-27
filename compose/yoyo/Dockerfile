FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./yoyo/ /app/
COPY ./migrations/ /app/migrations

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "apply.py"]

RUN adduser --system --no-create-home nonroot
USER nonroot
