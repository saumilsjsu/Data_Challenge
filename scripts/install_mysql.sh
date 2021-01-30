#!/bin/bash

# TODO: Should be downloading this from an AWS key store
#		rather than hardcoding it.
MYSQL_PASSWORD="root"

# Download and Install the Latest Updates for the OS
apt-get update && apt-get upgrade -y

export DEBIAN_FRONTEND="noninteractive"

debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_PASSWORD"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_PASSWORD"

apt-get install -y mysql-server-8.0

mysql_secure_installation

sed -i 's/127\.0\.0\.1/0\.0\.0\.0/g' /etc/mysql/my.cnf
sed -i '/\[mysqld\]/a\lower_case_table_names=1' /etc/mysql/my.cnf
echo "MySQL Password set to '${MYSQL_PASSWORD}'. Remember to delete ~/.mysql.passwd" | tee ~/.mysql.passwd; 

