FROM python:3.11.4-alpine

WORKDIR /erms

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "sh","./start.sh"]

