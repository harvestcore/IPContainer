FROM python:3.6

COPY . ./ipc

RUN pip install --upgrade pip
RUN cd ./ipc && pip3 install -r requirements.txt

ENTRYPOINT cd ./ipc && python3 application.py
