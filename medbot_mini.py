import streamlit as st
import datetime
from medicine_data import med_db  # ✅ Importing the database from external file

# ------------------ PAGE TITLE ------------------ #
st.set_page_config(page_title="MedBot Mini", page_icon="💊")
st.title("💊 MedBot Mini – Your Medication Companion")

# ------------------ MEDICINE EXPLAINER ------------------ #
st.header("1️⃣ Ask About a Medicine")

query = st.text_input("Enter the name of your medicine (e.g., Metformin 500mg)")

if query:
    key = query.lower().split()[0]
    if key in med_db:
        data = med_db[key]
        st.success(f"📌 **Use:** {data['use']}")
        st.info(f"💊 **How to Take:** {data['how_to_take']}")
        st.warning(f"⚠️ **Side Effects:** {data['side_effects']}")
        st.markdown(f"💡 **Tip:** {data['tip']}")
    else:
        st.error("❌ Sorry, I don't recognize that medicine yet.")

# ------------------ DAILY MEDICATION TRACKER ------------------ #
st.header("2️⃣ Daily Medication Tracker")

# Initialize the list
if "med_list" not in st.session_state:
    st.session_state.med_list = []

# Add a new medicine entry
with st.form("add_medicine_form"):
    med_name = st.text_input("Medicine Name (e.g., Losartan)")
    med_time = st.time_input("Time to Take", value=datetime.time(9, 0))
    add_btn = st.form_submit_button("➕ Add Medicine")

    if add_btn and med_name:
        st.session_state.med_list.append((med_name, med_time))
        st.success(f"✅ Added: {med_name} at {med_time.strftime('%I:%M %p')}")

# Display the list
if st.session_state.med_list:
    st.subheader("📋 Your Medicine Schedule for Today")
    for i, (name, time) in enumerate(st.session_state.med_list, 1):
        st.write(f"{i}. {name} ⏰ {time.strftime('%I:%M %p')}")

# ------------------ REMINDER SIMULATION ------------------ #
st.header("3️⃣ Reminder Simulation")

now = datetime.datetime.now().time()
st.info("⏳ Checking for upcoming medicines in the next 1 hour...")

for med, time in st.session_state.med_list:
    delta = abs(datetime.datetime.combine(datetime.date.today(), time) -
                datetime.datetime.combine(datetime.date.today(), now)).seconds
    if delta < 3600:
        st.warning(f"🔔 Reminder: It’s time to take **{med}** at {time.strftime('%I:%M %p')}")

# ------------------ FOOTER ------------------ #
st.markdown("---")
st.caption("Made with ❤️ by NAZEYA NEHAL")
