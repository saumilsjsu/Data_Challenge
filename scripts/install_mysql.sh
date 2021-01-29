#!/bin/bash


## Download mysql tar installer ##
#curl https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.23-macos10.15-x86_64.tar.gz -o mysql-8.0.23.tar.gz

## Unpack ##
rm -rf /usr/local/mysql
mkdir -p /usr/local/mysql
cp mysql-8.0.23.tar.gz /usr/local

## Install it ##

#groupadd mysql
#useradd -r -g mysql -s /bin/false mysql
cd /usr/local
tar zxvf mysql-8.0.23.tar.gz 
ln -s mysql-8.0.23 mysql
cd mysql
rm -rf mysql-files
mkdir mysql-files
chown mysql:mysql mysql-files
chmod 750 mysql-files
bin/mysqld --initialize --user=mysql
bin/mysql_ssl_rsa_setup

## Start the server ## 
bin/mysqld_safe --user=mysql &   ## Or could use "systemctl start mysqld"
