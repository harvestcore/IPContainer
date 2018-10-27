FROM python:3

COPY . .

RUN pip install --upgrade pip
RUN pip3 install -r ./IPContainer/requirements.txt
