import streamlit as st
import time
from datetime import datetime

# 1. CONFIGURATION ÉLITE
st.set_page_config(
    page_title="PRO Focus AI - Suite Commerciale",
    page_icon="💰",
    layout="wide"
)

# Style Premium
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1fd363; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. SÉCURITÉ ANTI-ERREUR (Nettoyage de la mémoire)
if 'taches' not in st.session_state or (len(st.session_state.taches) > 0 and isinstance(st.session_state.taches[0], str)):
    st.session_state.taches = []

st.title("🚀 PRO Focus AI : L'Elite de la Productivité")
st.write("---")

# 3. ARCHITECTURE COMMERCIALE
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.header("📋 Gestion de Projet")
    
    nouvelle_tache = st.text_input("Objectif prioritaire :")
    priorite = st.selectbox("Niveau de priorité", ["Standard", "Urgent 🔥", "Critique 💎"])
    
    if st.button("Enregistrer l'objectif"):
        if nouvelle_tache:
            # On enregistre un dictionnaire propre
            st.session_state.taches.append({
                "nom": nouvelle_tache, 
                "priorite": priorite, 
                "heure": datetime.now().strftime("%H:%M")
            })
            st.rerun()

    # Affichage sécurisé
    for i, t in enumerate(st.session_state.taches):
        with st.expander(f"{t['priorite']} - {t['nom']}"):
            st.write(f"Ajouté à : {t.get('heure', 'Heure inconnue')}")
            if st.button("Marquer comme terminé", key=f"done_{i}"):
                st.session_state.taches.pop(i)
                st.rerun()

with col2:
    st.header("⚡ Turbo Focus")
    duree = st.select_slider("Session de travail (min)", options=[1, 15, 25, 45, 60, 90], value=25)
    
    if st.button("LANCER LE MODE ELITE"):
        sec = duree * 60
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(sec, -1, -1):
            m, s = divmod(i, 60)
            status_text.metric("TEMPS RESTANT", f"{m:02d}:{s:02d}")
            progress_bar.progress(1 - (i / sec))
            time.sleep(1)
        
        st.balloons()
        st.success("SESSION TERMINÉE - REVENU ESTIMÉ : +50€")
        st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)

with col3:
    st.header("🤖 Coach IA (Beta)")
    st.info("L'IA analyse votre rythme.")
    if len(st.session_state.taches) > 3:
        st.warning("⚠️ Trop de tâches ! Concentrez-vous sur l'objectif Critique.")
    else:
        st.success("✅ Charge de travail optimale.")

st.write("---")
st.caption("© 2026 Neil Corporation - Version Enterprise Cloud v2.0")
