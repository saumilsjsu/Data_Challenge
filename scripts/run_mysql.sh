#!/bin/bash

MYSQL_PASSWORD="root"
service mysql restart
mysql -uroot -proot -e "CREATE USER 'root'@'root'; GRANT ALL ON *.* TO 'root'@'root'; FLUSH PRIVILEGES;"
service mysql stop

# runs the mysql daemon in foreground
mysqld_safe