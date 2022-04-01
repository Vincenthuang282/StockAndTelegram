#!/bin/bash

python3 /home/vincenthuang282/StockAndTelegram/Fetch_Data_to_database.py 
rm /home/vincenthuang282/StockAndTelegram/result_file/*
python3 /home/vincenthuang282/StockAndTelegram/data_analyist.py 



git config --global user.email "vincenthuang282@gmail.com"
git config --global user.name "Vincent Huang"
git add *
git commit -m "refresh the data"
git push https://Vincenthuang282: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@github.com/Vincenthuang282/StockAndTelegram.git --all
