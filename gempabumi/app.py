import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Gempa Bumi Dunia",
)

st.title("Gempa Bumi Dunia")
st.write("Visualisasi data gempa bumi berdasarkan kekuatan dan lokasi.")

# Membaca file CSV yang berada satu folder dengan app.py
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "all_month.csv"

data = pd.read_csv(csv_path)

# Informasi utama
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Data Gempa", len(data))

with col2:
    st.metric("Magnitudo Terbesar", round(data["mag"].max(), 1))

# Filter
st.subheader("Filter Gempa")

mag = st.slider(
    "Pilih Magnitudo Gempa",
    0.0, 8.0, 2.0
)

filtered_data = data[data["mag"] >= mag]

st.write("Jumlah gempa yang ditampilkan:", len(filtered_data))

# Peta
st.subheader("Peta Lokasi Gempa")

st.map(
    filtered_data,
    latitude="latitude",
    longitude="longitude"
)