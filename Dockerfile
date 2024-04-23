FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3

RUN apt-get install -y sqlite

COPY ./server-client/server.py /app/server.py
COPY ./server-client/database.py /app/database.py
COPY ./server-client/sc.sh /app/sc.sh
WORKDIR /app

RUN chmod +x /app/server.py
RUN chmod +x /app/sc.sh

RUN echo "server ITs RUNNING"

CMD ["python3", "server.py"]
