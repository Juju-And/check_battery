#!/usr/bin/env python
import time
import os
import argparse


class Battery:
    def get_capacity(self):
        source_capacity = open('/sys/class/power_supply/BAT0/capacity', "r")
        if source_capacity.mode == 'r':
            capacity = int(source_capacity.read())
            print(capacity)
        return capacity

    def is_charging(self):
        source_charging_status = open('/sys/class/power_supply/BAT0/status', "r")
        status = False
        charging_status = ''
        if source_charging_status.mode == 'r':
            charging_status = source_charging_status.read()
            print(charging_status)

        if charging_status == "Charging\n":
            print("Charging in process")
            status = True
        elif charging_status == "Discharging\n":
            print("Not charging")
            status = False
        else:
            status = False
        return status


class Program:
    def run(self):
        parser = argparse.ArgumentParser(description='A help to check_battery.py script.')
        parser.add_argument("-s", default=20, type=int, help="This is the minimum charge level")
        parser.add_argument("-e", default=80, type=int, help="This is the maximum charge level")
        parser.add_argument("-o", action='store_true', help="Perform only once")

        args = parser.parse_args()

        checker = CheckBattery(args.s, args.e)
        if args.o:
            checker.check()
        else:
            while True:
                checker.check()
                time.sleep(5)


class CheckBattery:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.battery = Battery()

    def check(self):
        capacity = self.battery.get_capacity()
        if self.battery.is_charging():
            if capacity >= self.end:
                # print("Charged to 80%. Please unplug!")
                os.system("espeak 'Please unplug!'")
                os.system('notify-send "BATTERY WARNING" "Charged to {}%. Please unplug!"'.format(self.end))
        else:
            if capacity <= self.start:
                # print("Battery level 20%. Please plug in!")
                os.system("espeak 'Please plug in!'")
                os.system('notify-send "BATTERY WARNING" "Battery level {}%. Please plug in!"'.format(self.start))


program = Program()
program.run()
