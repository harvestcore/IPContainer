FROM python:3.6

COPY . ./ipc

RUN pip install --upgrade pip
RUN cd ./ipc && pip3 install -r requirements.txt

EXPOSE 5000

CMD cd ./ipc && python3 application.py