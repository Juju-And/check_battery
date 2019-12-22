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
