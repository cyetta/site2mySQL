# site table to mysql table

Example of parsing table from site into MySQL database table

Тестовое задание 5.  
Напишите пожалуйста функцию, которая запишет результат вывода из задачи 2 в таблицу MySQL

Результат работы программы
![Pic2!](/pic/pic2.png)

Если у Вас установлена\есть доступ к БД используйте свое  
В моем случае для тестовой БД я использовал докер контейнер mysql.  
Необходимо наличие установленного [docker и docker-compose](https://www.docker.com/)  

Запуск БД:  
$ docker-compose up -d

Проверка:  
$ docker-compose ps -a


![Запуск БД в контейнере mysql!](/pic/pic1.png)

Для подключения к БД потребовалось установить:  
$ pip install mysql-connector-python  
Иначе возникала ошибка  
mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported