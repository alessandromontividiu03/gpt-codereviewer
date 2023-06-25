FROM python:3.10-slim

RUN pip3 install --upgrade pip
RUN mkdir /gpt-codereviewer
WORKDIR /gpt-codereviewer
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 80