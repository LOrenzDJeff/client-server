#!/bin/bash

while true; do
  clear
  echo "Таблица"
  echo "ID|data"
  echo "------------------------"
  sqlite3 example.db "SELECT * FROM numbers;"
  echo "------------------------"
  sleep 2
done
