#!/bin/bash

#----INIT----
cat welcome
echo
echo 'Start installation...'
echo 'Updating source lists...'
sudo apt-get update
#----INSTALL BASIC TOOLS----
echo 'Installng basic tools...'
sudo apt-get install curl -y
sudo apt install git -y
sudo apt install wget -y
#----END INSTALLATION----
#----END INIT----

