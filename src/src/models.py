from datetime import datetime

class Appointment:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
        self.reminded = False

    def get_datetime(self):
        return datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "reminded": self.reminded
        }

    @staticmethod
    def from_dict(data):
        appointment = Appointment(
            data["title"],
            data["date"],
            data["time"]
        )
        appointment.reminded = data.get("reminded", False)
        return appointment
