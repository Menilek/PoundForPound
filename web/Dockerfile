FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --user --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]