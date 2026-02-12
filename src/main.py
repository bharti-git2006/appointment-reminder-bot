from models import Appointment
from storage import load_appointments, save_appointments
from datetime import datetime

def add_appointment(appointments):
    title = input("Enter appointment title: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM in 24hr format): ")

    try:
        # Validate datetime format
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format.")
        return

    appointment = Appointment(title, date, time)
    appointments.append(appointment)
    save_appointments(appointments)
    print("Appointment added successfully.\n")

def view_appointments(appointments):
    if not appointments:
        print("No appointments found.\n")
        return

    print("\nYour Appointments:")
    for idx, appt in enumerate(appointments):
        print(f"{idx + 1}. {appt.title} on {appt.date} at {appt.time}")
    print()

def main():
    appointments = load_appointments()

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
