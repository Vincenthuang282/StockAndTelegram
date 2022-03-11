#!/bin/bash
sudo yum -y install git
git clone https://github.com/Vincenthuang282/StockAndTelegram.git
cd /home/vincenthuang282/StockAndTelegram/
sudo yum -y install python3
sudo yum -y install python3-pip
sudo pip3 install --upgrade pip
pip3 install -r requirements.txt 
nohup python3 /home/vincenthuang282/StockAndTelegram/main.py &
