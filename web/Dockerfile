FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]

# CMD gunicorn app:app --bind 0.0.0.0:5000 --reload