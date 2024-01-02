FROM python:3.11.3

WORKDIR /app

RUN git clone https://github.com/juansbarreto/tic-tac-toe

WORKDIR /app/tic-tac-toe

RUN pip install -r requirements.txt

CMD ["python", "tic-tac-toe.py"]
