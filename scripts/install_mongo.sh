#!/bin/bash

# set noninteractive installation
export DEBIAN_FRONTEND=noninteractive

# install wget
apt-get -y install wget

#install tzdata package
apt-get install -y tzdata

# set your timezone
ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
dpkg-reconfigure --frontend noninteractive tzdata

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
apt-get update
apt-get install -y mongodb-org

# Although you can specify any available version of MongoDB, apt-get will 
# upgrade the packages when a newer version becomes available. To prevent 
# unintended upgrades, you can pin the package at the currently installed 
# version.
echo "mongodb-org hold" | dpkg --set-selections
echo "mongodb-org-server hold" | dpkg --set-selections
echo "mongodb-org-shell hold" | dpkg --set-selections
echo "mongodb-org-mongos hold" | dpkg --set-selections
echo "mongodb-org-tools hold" | dpkg --set-selections

# create data directories for mongod
mkdir /data
mkdir /data/db