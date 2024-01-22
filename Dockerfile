FROM python:3.10.12-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/./moving_donuts.py"]
