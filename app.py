import streamlit as st
import time
from datetime import datetime

# CONFIGURATION COMMERCIALE
st.set_page_config(page_title="PRO Focus AI", page_icon="💰", layout="wide")

# FIX : On nettoie la mémoire si l'ancien format est détecté
if 'taches' not in st.session_state or (len(st.session_state.taches) > 0 and isinstance(st.session_state.taches[0], str)):
    st.session_state.taches = []

st.title("🚀 PRO Focus AI : L'Elite")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Objectifs")
    nouveau = st.text_input("Ajouter un objectif :")
    priorite = st.selectbox("Priorité", ["Standard", "Urgent 🔥", "Critique 💎"])
    
    if st.button("Enregistrer"):
        if nouveau:
            st.session_state.taches.append({"nom": nouveau, "prio": priorite})
            st.rerun()

    for i, t in enumerate(st.session_state.taches):
        st.write(f"🔹 **{t['prio']}** : {t['nom']}")
        if st.button("Fait", key=f"f_{i}"):
            st.session_state.taches.pop(i)
            st.rerun()

with col2:
    st.header("⏳ Turbo Focus")
    duree = st.slider("Minutes", 1, 60, 25)
    if st.button("DÉMARRER"):
        sec = duree * 60
        barre = st.progress(0)
        for s in range(sec, -1, -1):
            barre.progress(1 - (s / sec))
            time.sleep(1)
        st.balloons()
