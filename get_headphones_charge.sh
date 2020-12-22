#!/bin/bash

cd /home/roman/Applications/Bluetooth_Headset_Battery_Level/

export dev_info=$(bluetoothctl info)
dev_info=$(python ./get_bt_info.py)

if [[ $dev_info == *":"* ]]; then
    python ./cacher.py $dev_info $1
fi
