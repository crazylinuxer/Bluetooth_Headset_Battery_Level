#!/bin/bash

cd /home/roman/Applications/Bluetooth_Headset_Battery_Level/

if [[ $1 == *":"* ]]; then
    . ./.venv/bin/activate
    printf "🎧 %s" $(./bluetooth_battery.py $1.1)
fi
