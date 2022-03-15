#!/bin/bash
sudo yum -y install python3
sudo yum -y install python3-pip
sudo pip3 install --upgrade pip
pip3 install -r requirements.txt 
nohup python3 /home/vincenthuang282/StockAndTelegram/main.py &
exit
