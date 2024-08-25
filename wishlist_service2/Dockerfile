FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV DATABASE_URL=/app/data/wishlist.sqlite

CMD ["python", "app.py"]
