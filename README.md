# 💊 MedBot Mini – Your Medication Companion 🩺

MedBot Mini is a **Streamlit-based application** designed to help users manage their medications efficiently.  
It provides detailed information about medicines, tracks daily medication schedules, and simulates reminders to ensure timely intake.

---

## 🚀 Getting Started

1️⃣ Clone the Repository
```bash
git clone https://github.com/nazeyanehal/MedBot-Mini
cd MedBot-Mini
```

2️⃣ Install Dependencies
```bash
pip install streamlit
```

3️⃣ Run the App
```bash
streamlit run app.py  # replace app.py with your main file name
Open the URL shown in your browser to start using MedBot Mini.
```

### ⚙️ Features
1️⃣ Ask About a Medicine
Enter the name of a medicine (e.g., Metformin 500mg)

Receive:

📌 Use

💊 How to Take

⚠️ Side Effects

💡 Tips

If the medicine is not recognized, a friendly error message is displayed.

2️⃣ Daily Medication Tracker
Add medicines and their intake times

View a daily schedule 📋

Store and track medicines in real-time using st.session_state

3️⃣ Reminder Simulation
Checks for medicines due in the next hour ⏰

Sends visual reminders: 🔔 "It’s time to take Medicine Name"

### 📂 Project Structure
bash
Copy code
MedBot-Mini/
│
├── app.py             # Main Streamlit app
├── medicine_data.py   # Database of medicines
└── README.md          # Project README

### 📝 How It Works
Medicines are retrieved from a pre-defined database (med_db)

User inputs are processed in real-time with Streamlit widgets

Reminders are simulated based on the current time and scheduled medicine times
