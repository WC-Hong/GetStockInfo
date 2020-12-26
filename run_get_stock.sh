#!/bin/bash

STOCK=2610
TODAY=$(date +"%d-%m-%Y")
python3 get_stock_info.py $STOCK $TODAY
