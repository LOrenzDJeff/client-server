import unittest
import threading
import socket
import sqlite3
import os
import time
from database import cratedatabase, newcell, databaseset
# Импортируем функции, которые будем тестировать
#from server import cratedatabase, database, handle_client

# Класс для тестирования создания базы данных
class TestCreateDatabase(unittest.TestCase):
    def test_create_database(self):
        # Проверяем, что база данных успешно создана
        cratedatabase()
        con = sqlite3.connect('example.db')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='numbers'")
        result = cursor.fetchone()
        #print(result)
        self.assertIsNotNone(result)  # Убедимся, что таблица была создана
        #print(self.assertIsNotNone(result))
        con.close()
        os.remove("example.db")

# Класс для тестирования обновления данных в базе данных
class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Подготовим базу данных для тестов
        cratedatabase()
        newcell(1)


    def test_database(self):
        # Проверяем, что база данных обновляется корректно
        databaseset(5, 1)  # Увеличим значение на 5 для id=1
        con = sqlite3.connect('example.db')
        cursor = con.cursor()
        cursor.execute("SELECT value FROM numbers WHERE id = 1")
        result = cursor.fetchone()[0]
        self.assertEqual(result, 5)  # Убедимся, что значение изменилось
        con.close()
        os.remove("example.db")

# Класс для тестирования обработчика клиента
class TestClientServerConnection(unittest.TestCase):

    def setUp(self):
        self.host = "server"
        self.port = 12345
        self.success = True 

    def tearDown(self):
        if self.success:
            print("OK, test_3")
        else:
            print("FALSE, test_3")
        #exit()

    def test_client_server_connection(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        time.sleep(1)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))

        client.send(b"10 a")
        response = client.recv(1024)

        if response is None or len(response) == 0:
            self.success = False
            print("Ответ от сервера не был получен")
        else:
            print("Успешно установлена связь между клиентом и сервером")
        client.close()
        time.sleep(70)

    def run_server(self):
       print("Жми рычаг")

if __name__ == '__main__':
    unittest.main()
