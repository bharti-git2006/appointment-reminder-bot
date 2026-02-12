import json
import os
from models import Appointment

DATA_FILE = "data/appointments.json"

def load_appointments():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        return [Appointment.from_dict(item) for item in data]

def save_appointments(appointments):
    with open(DATA_FILE, "w") as file:
        json.dump([appt.to_dict() for appt in appointments], file, indent=4)
