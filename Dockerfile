FROM python:3.6

COPY . ./ipc

RUN pip install --upgrade pip
RUN cd ./ipc && pip3 install -r requirements.txt

ENV MYSQL_KEY="mysql+mysqlconnector://sql2264325:yY9*dF2%@sql2.freemysqlhosting.net:3306/sql2264325"
ENV SECRET_KEY="rQsgiA2EupfZTo7WIBY61CmHMWrUTvRBl6JiITvp1GW2uyP5rhHWEh3KZAb3R2F7"

EXPOSE 5000

CMD cd ./ipc && python3 application.py