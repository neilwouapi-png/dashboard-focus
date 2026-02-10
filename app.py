import streamlit as st
import time

# --- CONFIGURATION PRO ---
st.set_page_config(page_title="PRO Focus AI", layout="wide")

# --- PROTECTION DE LA MÉMOIRE (SÉCURITÉ MAX) ---
if 'taches' not in st.session_state or not isinstance(st.session_state.taches, list):
    st.session_state.taches = []

# Si on détecte encore l'ancien format (texte au lieu de dictionnaire), on vide tout
if len(st.session_state.taches) > 0 and isinstance(st.session_state.taches[0], str):
    st.session_state.taches = []

st.title("🚀 PRO Focus AI : Business Edition")

# --- INTERFACE ---
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Objectifs de Profit")
    with st.form("ajout_tache"):
        nom = st.text_input("Nom de la tâche :")
        prio = st.select_slider("Priorité", options=["Basse", "Moyenne", "Haute", "CRITIQUE"])
        valider = st.form_submit_button("Ajouter à la liste")
        
        if valider and nom:
            st.session_state.taches.append({"nom": nom, "prio": prio})
            st.rerun()

    for i, t in enumerate(st.session_state.taches):
        if isinstance(t, dict): # Double vérification de sécurité
            st.info(f"**[{t['prio']}]** {t['nom']}")
            if st.button(f"Terminer {i}", key=f"btn_{i}"):
                st.session_state.taches.pop(i)
                st.rerun()

with col2:
    st.header("⏳ Session de Performance")
    minutes = st.number_input("Durée (min)", 1, 120, 25)
    if st.button("LANCER LE TURBO"):
        barre = st.progress(0)
        for p in range(101):
            time.sleep((minutes * 60) / 100)
            barre.progress(p)
        st.balloons()
        st.success("Argent généré ! Session terminée.")

# Bouton de secours en bas de page
if st.sidebar.button("⚠️ RESET TOTAL (En cas de bug)"):
    st.session_state.clear()
    st.rerun()
