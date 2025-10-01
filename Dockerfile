FROM python:3.12.3

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY src /app

CMD python app/app.py