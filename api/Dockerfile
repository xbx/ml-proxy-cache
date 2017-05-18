FROM python:3

RUN pip install flasgger

RUN mkdir /api/
WORKDIR /api/

COPY app.py /api/

EXPOSE 5000
ENV FLASK_APP=app.py
CMD flask run
