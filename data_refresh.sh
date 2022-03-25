#!/bin/bash

python3 /home/vincenthuang282/StockAndTelegram/Fetch_Data_to_database.py 
rm /home/vincenthuang282/StockAndTelegram/result_file/*
python3 /home/vincenthuang282/StockAndTelegram/data_analyist.py 
git add *
git commit -m "refresh the data"
git push https://vincenthuang282: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@github.com/vincenthuang282/StockAndTelegram.git --all
