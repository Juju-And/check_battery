#!/usr/bin/env python
import time
import os
import argparse
from checkbattery import CheckBattery


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
