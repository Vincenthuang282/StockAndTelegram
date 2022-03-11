#!/bin/bash

python3 /home/vincenthuang282/StockAndTelegram/Fetch_Data_to_database.py 
rm /home/vincenthuang282/StockAndTelegram/result_file/*
python3 /home/vincenthuang282/StockAndTelegram/data_analyist.py 
