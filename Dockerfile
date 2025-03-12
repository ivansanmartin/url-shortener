FROM python:3.11.4-slim


WORKDIR /code

RUN apt-get update && apt-get install -y git

COPY ./requirements.txt /code/requirements.txt
COPY ./.env /code/.env


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get remove -y git && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "8080"]