FROM python:3.12-alpine

ENV FLASK_APP=flaskr

WORKDIR /app

COPY . ./flaskr
RUN pip install --no-cache-dir -r flaskr/requirements.txt

EXPOSE 5000

RUN flask init-db

CMD ["flask", "run", "--host=0.0.0.0"]