FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install virtualenv

RUN virtualenv .venv

RUN ./.venv/bin/python -m pip install -r requirements.txt

CMD ["./test.sh"]
