print("Scheduler file imported")
import time
from datetime import datetime
from storage import save_appointments

def start_scheduler(appointments):
    print("Reminder system started...\n")

    while True:
        now = datetime.now()

        for appt in appointments:
            appointment_time = appt.get_datetime()

            if not appt.reminded and now >= appointment_time:
                print(f"\n🔔 Reminder: {appt.title} is scheduled now!")
                appt.reminded = True
                save_appointments(appointments)

        time.sleep(15)  # Check every 15 seconds
