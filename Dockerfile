FROM python:3.12
WORKDIR /check_weather

COPY ./requirements.txt /check_weather/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /check_weather/requirements.txt

COPY ./app /check_weather/app

CMD fastapi dev "./main.py" --host 0.0.0.0