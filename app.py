#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:54:12 2023

@author: nizam
"""

import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


# Load the saved model
parkinsons_model = pickle.load(
    open(
        "parkinsons_model.sav",
        "rb",
    )
)

# Sidebar for navigation
with st.sidebar:
    st.title("Sistem Prediksi Penyakit")
    selected = option_menu(
        "Pilihan Menu",
        [
            "Penjelasan Dataset",
            "Prediksi Parkinson",
        ],
        icons=["person"],
        default_index=0,
    )
# Load the dataset
parkinsons_data = pd.read_csv(
    "parkinsons.csv"
)
# Penjelasan Dataset
if selected == "Penjelasan Dataset":
    # page title
    st.title("Penjelasan Dataset Parkinson's Disease")

    # Penjelasan tentang dataset Parkinson's Disease
    st.write(
        "Dataset Parkinson's Disease adalah kumpulan data yang berisi informasi tentang pasien "
        + "yang memiliki atau tidak memiliki penyakit Parkinson. Penyakit Parkinson adalah gangguan "
        + "saraf yang memengaruhi gerakan fisik seseorang. Aplikasi ini memprediksi apakah seseorang "
        + "mungkin memiliki penyakit Parkinson berdasarkan atribut suara."
    )

    # Daftar atribut dataset Parkinson's Disease
    st.header("Atribut Dataset:")
    st.write("1. MDVP:Fo(Hz): Frekuensi fundamental rata-rata dalam Hertz (Hz).")
    st.write("2. MDVP:Fhi(Hz): Frekuensi tertinggi dalam Hertz (Hz).")
    st.write("3. MDVP:Flo(Hz): Frekuensi terendah dalam Hertz (Hz).")
    st.write("4. MDVP:Jitter(%): Persentase jitter dalam sinyal suara.")
    st.write("5. MDVP:Jitter(Abs): Jitter absolut dalam sinyal suara.")
    st.write("6. MDVP:RAP: Average absolute perturbation dalam siklus suara.")
    st.write("7. MDVP:PPQ: Average absolute perturbation dalam siklus suara (yang berbeda dengan MDVP:RAP).")
    st.write("8. Jitter:DDP: Jitter dalam suara, yang merupakan perpanjangan dari MDVP:Jitter.")
    st.write("9. MDVP:Shimmer: Shimmer adalah ukuran dari perubahan dalam amplitudo dalam suara.")
    st.write("10. MDVP:Shimmer(dB): Shimmer dalam desibel (dB). Ini adalah ukuran perubahan amplitudo dalam dB.")

    # Tambahkan contoh data
    st.header("Contoh Data:")
    st.write("Berikut adalah beberapa contoh data dari dataset:")
    st.write(parkinsons_data.head())



    # Tambahkan tautan atau referensi dataset jika ada
    st.header("Referensi Dataset:")
    st.write(
        "Dataset ini diambil dari [Kaggle](https://www.kaggle.com/). Dataset asli dapat diakses [di sini](https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set). "
        + "Informasi tambahan tentang penyakit Parkinson dapat ditemukan di [Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_disease)."
    )

    # Penjelasan tentang penyakit Parkinson
    st.title("Penyakit Parkinson")
    st.write(
        "Parkinson's Disease atau penyakit Parkinson adalah gangguan saraf yang memengaruhi gerakan fisik "
        + "seseorang. Gejalanya termasuk tremor (getaran), kaku otot, kesulitan bergerak, dan masalah keseimbangan. "
        + "Pemantauan dan diagnosis dini dapat membantu dalam pengelolaan penyakit ini."
    )


# Parkinson's Prediction Page
if selected == "Prediksi Parkinson":
    # page title
    st.title("Prediksi Parkinson dengan ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        RAP = st.text_input("MDVP:RAP")

    with col2:
        PPQ = st.text_input("MDVP:PPQ")

    with col3:
        DDP = st.text_input("Jitter:DDP")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col3:
        APQ = st.text_input("MDVP:APQ")

    with col4:
        DDA = st.text_input("Shimmer:DDA")

    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col4:
        spread1 = st.text_input("spread1")

    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        D2 = st.text_input("D2")

    with col2:
        PPE = st.text_input("PPE")

    # code for Prediction
    parkinsons_diagnosis = ""

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [
                [
                    fo,
                    fhi,
                    flo,
                    Jitter_percent,
                    Jitter_Abs,
                    RAP,
                    PPQ,
                    DDP,
                    Shimmer,
                    Shimmer_dB,
                    APQ3,
                    APQ5,
                    APQ,
                    DDA,
                    NHR,
                    HNR,
                    RPDE,
                    DFA,
                    spread1,
                    spread2,
                    D2,
                    PPE,
                ]
            ]
        )

        if parkinsons_prediction[0] == 0:
            parkinsons_diagnosis = "Orang tersebut tidak memiliki penyakit Parkinson"
        else:
            parkinsons_diagnosis = "Orang tersebut memiliki penyakit Parkinson"

    st.success(parkinsons_diagnosis)
    