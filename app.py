import streamlit as st
import time
import pandas as pd
from datetime import datetime

# Configuration Expert du Dashboard
st.set_page_config(
    page_title="PRO Focus AI - Suite Commerciale",
    page_icon="💰",
    layout="wide"
)

# Style CSS personnalisé pour un look Premium
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1fd363; color: black; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 PRO Focus AI : L'Elite de la Productivité")
st.write("---")

# --- ARCHITECTURE COMMERCIALE : 3 COLONNES ---
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.header("📋 Gestion de Projet")
    if 'taches' not in st.session_state:
        st.session_state.taches = []
    
    nouvelle_tache = st.text_input("Objectif prioritaire :")
    priorite = st.selectbox("Niveau de priorité", ["Standard", "Urgent 🔥", "Critique 💎"])
    
    if st.button("Enregistrer l'objectif"):
        if nouvelle_tache:
            st.session_state.taches.append({"nom": nouvelle_tache, "priorite": priorite, "heure": datetime.now().strftime("%H:%M")})
            st.rerun()

    for i, t in enumerate(st.session_state.taches):
        with st.expander(f"{t['priorite']} - {t['nom']}"):
            st.write(f"Ajouté à : {t['heure']}")
            if st.button("Marquer comme terminé", key=f"done_{i}"):
                st.session_state.taches.pop(i)
                st.balloons()
                st.rerun()

with col2:
    st.header("⚡ Turbo Focus")
    duree = st.select_slider("Session de travail (min)", options=[15, 25, 45, 60, 90], value=25)
    
    if st.button("LANCER LE MODE ELITE"):
        sec = duree * 60
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(sec, -1, -1):
            m, s = divmod(i, 60)
            status_text.metric("TEMPS RESTANT", f"{m:02d}:{s:02d}")
            progress_bar.progress(1 - (i / sec))
            time.sleep(1)
        
        st.success("SESSION TERMINÉE - REVENU GÉNÉRÉ ESTIMÉ : +50€")
        # Son d'alerte
        st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)

with col3:
    st.header("🤖 Coach IA (Beta)")
    st.info("L'IA analyse votre rythme de travail pour maximiser vos profits.")
    st.write("**Conseil du jour :**")
    if len(st.session_state.taches) > 3:
        st.warning("Trop de tâches ! Concentrez-vous sur l'objectif 'Critique' pour éviter le burnout.")
    else:
        st.success("Charge de travail optimale. Votre cerveau est à 100% de ses capacités.")

# --- FOOTER COMMERCIAL ---
st.write("---")
st.caption("© 2026 Neil Corporation - Version Enterprise Cloud de Haute Performance")
