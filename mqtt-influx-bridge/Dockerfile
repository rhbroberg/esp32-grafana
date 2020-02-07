FROM python:rc-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY listener.py .

CMD [ "python", "./listener.py" ]

