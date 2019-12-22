#!/usr/bin/env python
import time
import os
import argparse

parser = argparse.ArgumentParser(description='A help to check_battery.py script.')
parser.add_argument("-s", default=20, type=int, help="This is the minimum charge level")
parser.add_argument("-e", default=80, type=int, help="This is the maximum charge level")

args = parser.parse_args()
print(args.e)

while True:
    time.sleep(5)
    # print("printed after 5 sec")
    source_capacity = open('/sys/class/power_supply/BAT0/capacity', "r")
    source_charging_status = open('/sys/class/power_supply/BAT0/status', "r")
    if source_capacity.mode == 'r':
        capacity = int(source_capacity.read())
    print(capacity)

    if source_charging_status.mode == 'r':
        charging_status = source_charging_status.read()
    print(charging_status)

    if charging_status == "Charging\n":
        print("Charging in process")
        if capacity >= args.e:
            # print("Charged to 80%. Please unplug!")
            os.system("espeak 'Please unplug!'")
            os.system(('notify-send "BATTERY WARNING" "Charged to {}%. Please unplug!"').format(args.e))

    elif charging_status == "Discharging\n":
        print("Not charging")
    if capacity <= args.s:
        # print("Battery level 20%. Please plug in!")
        os.system("espeak 'Please plug in!'")
        os.system('notify-send "BATTERY WARNING" "Battery level {}%. Please plug in!"'.format(args.s))

    else:
        print("Charging OK")
