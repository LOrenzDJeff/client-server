#!/bin/bash

python3 server.py > server.log 2>&1 &

sleep 5

for (( i=1; i<=5; i++ ))
do
    python3 client.py > client_$i.log 2>&1 &
    sleep 1
done


time=$(date +%s)
while [ $(($(date +%s) - $time)) -lt 60 ]; do
  clear
  echo "Таблица"
  echo "ID|data"
  echo "------------------------"
  sqlite3 example.db "SELECT * FROM numbers;"
  echo "------------------------"
  sleep 4
done

sleep 15
rm server.log
rm example.db
for (( i=1; i<=5; i++ ))
do
    rm client_$i.log
done