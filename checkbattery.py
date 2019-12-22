from battery import Battery
import os


class CheckBattery:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.battery = Battery()
        self.notification = None

    def check(self):
        capacity = self.battery.get_capacity()
        if self.battery.is_charging():
            if capacity >= self.end:
                os.system("espeak 'Please unplug!'")
                message = "Charged to {}%. Please unplug!".format(self.end)
                self.notify(message)
        else:
            if capacity <= self.start:
                os.system("espeak 'Please plug in!'")
                message = "Battery level {}%. Please plug in!".format(self.start)
                self.notify(message)

    def notify(self, message):
        if not self.notification == message:
            os.system('notify-send "BATTERY WARNING" "{}"'.format(message))
            self.notification = message
