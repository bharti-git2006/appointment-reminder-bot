📌 Appointment Reminder Bot
A simple Python-based command-line application that allows users to schedule appointments and receive automatic reminders at the scheduled time.
--> Features
-Add appointments with date & time
-View all scheduled appointments
-Automatic background reminder system
-Persistent storage using JSON
-Multithreading for real-time reminder checks

--> Tech Stack
-Python 3
-Threading
-JSON Storage
-Datetime module

--> Project Structure
appointment-reminder-bot/
│
├── data/
│   └── appointments.json
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── scheduler.py
│   ├── storage.py
│
└── README.md

--> How to Run
-Clone the repository:
-git clone <your-repo-link>
-Navigate to project folder:
-cd appointment-reminder-bot
-Run the application:
-python src/main.py

--> How It Works
-User inputs appointment details
-Data is stored in appointments.json
-A background scheduler thread continuously checks time
-When system time >= appointment time → reminder is triggered

--> Future Improvements
-GUI version
-Email notifications
-SMS integration
-Web version with Flask
-Notification sound alerts
