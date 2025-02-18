import streamlit as st
import joblib
import pandas as pd

# Memuat model dan scaler dari file pickle
posisi_unik = ['ST', 'LW', 'RW', 'CM', 'CB', 'LB', 'RB', 'GK']
models = {posisi: joblib.load(f'model_{posisi}.pkl') for posisi in posisi_unik}
scalers = {posisi: joblib.load(f'scaler_{posisi}.pkl') for posisi in posisi_unik}

# Fungsi untuk memprediksi posisi terbaik pemain berdasarkan input user
def prediksi_posisi_pemain(input_data):
    prediksi = {}
    for posisi, model in models.items():
        scaler = scalers[posisi]
        input_scaled = scaler.transform([input_data])
        prediksi[posisi] = model.predict(input_scaled)[0]
    posisi_terbaik = max(prediksi, key=prediksi.get)
    return posisi_terbaik

# Membuat aplikasi Streamlit
st.title("Prediksi Posisi Terbaik Pemain Sepak Bola")

# Input fitur dari user
age = st.number_input("Age", min_value=15, max_value=50, value=25)
height_cm = st.number_input("Height (cm)", min_value=140, max_value=220, value=180)
weight_kg = st.number_input("Weight (kg)", min_value=50, max_value=120, value=75)
attacking_crossing = st.number_input("Attacking Crossing", min_value=0, max_value=100, value=70)
attacking_finishing = st.number_input("Attacking Finishing", min_value=0, max_value=100, value=85)
attacking_heading_accuracy = st.number_input("Attacking Heading Accuracy", min_value=0, max_value=100, value=60)
attacking_short_passing = st.number_input("Attacking Short Passing", min_value=0, max_value=100, value=80)
attacking_volleys = st.number_input("Attacking Volleys", min_value=0, max_value=100, value=75)
skill_dribbling = st.number_input("Skill Dribbling", min_value=0, max_value=100, value=85)
skill_curve = st.number_input("Skill Curve", min_value=0, max_value=100, value=70)
skill_fk_accuracy = st.number_input("Skill FK Accuracy", min_value=0, max_value=100, value=65)
skill_long_passing = st.number_input("Skill Long Passing", min_value=0, max_value=100, value=80)
skill_ball_control = st.number_input("Skill Ball Control", min_value=0, max_value=100, value=85)
movement_acceleration = st.number_input("Movement Acceleration", min_value=0, max_value=100, value=90)
movement_sprint_speed = st.number_input("Movement Sprint Speed", min_value=0, max_value=100, value=85)
movement_agility = st.number_input("Movement Agility", min_value=0, max_value=100, value=80)
movement_reactions = st.number_input("Movement Reactions", min_value=0, max_value=100, value=85)
movement_balance = st.number_input("Movement Balance", min_value=0, max_value=100, value=80)
power_shot_power = st.number_input("Power Shot Power", min_value=0, max_value=100, value=75)
power_jumping = st.number_input("Power Jumping", min_value=0, max_value=100, value=70)
power_stamina = st.number_input("Power Stamina", min_value=0, max_value=100, value=80)
power_strength = st.number_input("Power Strength", min_value=0, max_value=100, value=85)
power_long_shots = st.number_input("Power Long Shots", min_value=0, max_value=100, value=75)
mentality_aggression = st.number_input("Mentality Aggression", min_value=0, max_value=100, value=70)
mentality_interceptions = st.number_input("Mentality Interceptions", min_value=0, max_value=100, value=65)
mentality_positioning = st.number_input("Mentality Positioning", min_value=0, max_value=100, value=60)
mentality_vision = st.number_input("Mentality Vision", min_value=0, max_value=100, value=70)
mentality_penalties = st.number_input("Mentality Penalties", min_value=0, max_value=100, value=65)
mentality_composure = st.number_input("Mentality Composure", min_value=0, max_value=100, value=70)
defending_marking_awareness = st.number_input("Defending Marking Awareness", min_value=0, max_value=100, value=50)
defending_standing_tackle = st.number_input("Defending Standing Tackle", min_value=0, max_value=100, value=55)
defending_sliding_tackle = st.number_input("Defending Sliding Tackle", min_value=0, max_value=100, value=50)

# Menggabungkan semua input fitur ke dalam satu list
input_user = [age, height_cm, weight_kg, attacking_crossing, attacking_finishing, attacking_heading_accuracy,
              attacking_short_passing, attacking_volleys, skill_dribbling, skill_curve, skill_fk_accuracy,
              skill_long_passing, skill_ball_control, movement_acceleration, movement_sprint_speed, movement_agility,
              movement_reactions, movement_balance, power_shot_power, power_jumping, power_stamina, power_strength,
              power_long_shots, mentality_aggression, mentality_interceptions, mentality_positioning, mentality_vision,
              mentality_penalties, mentality_composure, defending_marking_awareness, defending_standing_tackle,
              defending_sliding_tackle]

# Tombol untuk melakukan prediksi
if st.button("Prediksi Posisi Terbaik"):
    posisi_terbaik = prediksi_posisi_pemain(input_user)
    st.success(f"Posisi terbaik untuk pemain ini adalah: {posisi_terbaik}")