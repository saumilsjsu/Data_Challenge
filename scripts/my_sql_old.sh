#!/bin/bash

# GENERATE PASSOWRD 

PASS_MYSQL_ROOT=`openssl rand -base64 12`

installMySQL() {
	# MySQL
	echo -e "\n ${Cyan} Installing MySQL.."
	
	# set password with `debconf-set-selections` so you don't have to enter it in prompt and the script continues
	sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password ${PASS_MYSQL_ROOT}" # new password for the MySQL root user
	sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password ${PASS_MYSQL_ROOT}" # repeat password for the MySQL root user
	
	# DEBIAN_FRONTEND=noninteractive # by setting this to non-interactive, no questions will be asked
	DEBIAN_FRONTEND=noninteractive sudo apt -qy install mysql-server mysql-client
}

secureMySQL() {
	# secure MySQL install
	echo -e "\n ${Cyan} Securing MySQL.. "
	
	mysql --user=root --password=${PASS_MYSQL_ROOT} << EOFMYSQLSECURE
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
FLUSH PRIVILEGES;
EOFMYSQLSECURE

# NOTE: Skipped validate_password because it'll cause issues with the generated password in this script
}

# RUN

installMySQL
secureMySQL

echo -e "\n${Green} SUCCESS! MySQL password is: ${PASS_MYSQL_ROOT} "
