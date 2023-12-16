import psutil
from plyer import notification

def notify(title, message, timeout=2):
    notification.notify(title=title, message=message, timeout=timeout)

def battery_notification():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        if percent <= 80:
            notify("Plugged In", "For better battery life, charge up to 80%")
        elif percent == 100:
            notify("Plugged In", "Please unplug the charger. Battery is fully charged")
        else:
            notify("Plugged In", "Remove the charger. For better battery life, charge up to 80%")
    else:
        if percent <= 20:
            notify("Battery Reminder", "Your battery is running low. You might want to plug in your PC")
        elif 20 < percent <= 50:
            notify("Battery Reminder", f"Battery is at {percent}%.")
        elif percent == 100:
            notify("Battery Reminder", "Fully charged")
        else:
            notify("Battery Reminder", f"Battery is at {percent}%")

if __name__ == "__main__":
    battery_notification()
