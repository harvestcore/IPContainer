FROM python:3.6

COPY . .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
