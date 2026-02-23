<<<<<<< HEAD
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

=======
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

>>>>>>> c3b9c2e9a69cb93190c544f3660b30b7366941fb
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]