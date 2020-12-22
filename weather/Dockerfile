FROM python:3.9-alpine

WORKDIR /app

ADD . .
RUN pip install -r requirements.txt \
 && pip freeze

EXPOSE 8080

CMD ["python", "server.py"]
