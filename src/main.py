from models import Appointment
from storage import load_appointments, save_appointments
from scheduler import start_scheduler
from datetime import datetime
import threading

def add_appointment(appointments):
    title = input("Enter appointment title: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time_input = input("Enter time (HH:MM in 24hr format): ")

    try:
        datetime.strptime(f"{date} {time_input}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format.\n")
        return

    appointment = Appointment(title, date, time_input)
    appointments.append(appointment)
    save_appointments(appointments)
    print("Appointment added successfully.\n")

def view_appointments(appointments):
    if not appointments:
        print("No appointments found.\n")
        return

    print("\nYour Appointments:")
    for idx, appt in enumerate(appointments):
        status = "Reminded" if appt.reminded else "Pending"
        print(f"{idx + 1}. {appt.title} on {appt.date} at {appt.time} [{status}]")
    print()

def main():
    appointments = load_appointments()

    # Start scheduler in background thread
    scheduler_thread = threading.Thread(
        target=start_scheduler,
        args=(appointments,),
        daemon=True
    )
    scheduler_thread.start()

    while True:
        print("==== Appointment Reminder Bot ====")
        print("1. Add Appointment")
        print("2. View Appointments")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_appointment(appointments)
        elif choice == "2":
            view_appointments(appointments)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
