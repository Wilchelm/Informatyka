Warstwa rozszerzająca zapytania SQL o zapytania nieprecyzyjne

Baza danych Xampp 7.3.4.0

Jak jest problem z mysqlem z xamppa to:
1.	sudo service mysql stop
2.	sudo /opt/lampp/lampp restart

Klient do mysql w Xampp to http://127.0.0.1/phpmyadmin/index.php
Aplikacja python main.py -> http://127.0.0.1:4555/

W main.py:

def upload_csv_db(file_dir):
	mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")


to unix_socket=... to ścieżka do pliku z bazą



