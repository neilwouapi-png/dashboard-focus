import streamlit as st
import time
from datetime import datetime

# --- 1. CONFIGURATION DE LUXE ---
st.set_page_config(
    page_title="PRO Focus AI - Suite Commerciale",
    page_icon="💎",
    layout="wide"
)

# --- 2. SÉCURITÉ DE LA BASE DE DONNÉES TEMPORAIRE ---
if 'taches' not in st.session_state or not isinstance(st.session_state.taches, list):
    st.session_state.taches = []

# Nettoyage automatique des anciennes données incompatibles
if len(st.session_state.taches) > 0 and isinstance(st.session_state.taches[0], str):
    st.session_state.taches = []

# --- 3. MENU DE NAVIGATION PROFESSIONNEL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063302.png", width=100)
    st.title("💼 Neil Corp. Pro")
    st.markdown("---")
    menu = st.radio("Navigation Business", ["📈 Tableau de Bord", "💎 Devenir Membre PRO"])
    st.markdown("---")
    if st.button("⚠️ Réinitialiser l'App"):
        st.session_state.clear()
        st.rerun()

# --- 4. LOGIQUE DES PAGES ---

if menu == "💎 Devenir Membre PRO":
    st.title("📈 Maximisez vos Revenus")
    st.subheader("Choisissez la puissance de l'IA pour votre business")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("### Plan Standard\n**0€ / mois**\n\n- Accès au minuteur\n- 3 tâches prioritaires\n- Support Standard")
        st.button("Plan Actuel", disabled=True)
        
    with col_b:
        st.success("### Plan ELITE AI\n**19.99€ / mois**\n\n- Tâches Illimitées\n- Coach IA en temps réel\n- Alertes sonores Premium\n- Analyse de rentabilité")
        if st.button("S'ABONNER VIA STRIPE 🚀"):
            st.toast("Redirection vers le portail de paiement sécurisé...")

else:
    st.title("🚀 PRO Focus AI : Business Edition")
    st.write(f"Bienvenue, Neil. Performance du jour : **{datetime.now().strftime('%d/%m/%Y')}**")
    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.header("📋 Gestion de Projet")
        with st.form("form_tache", clear_on_submit=True):
            nom = st.text_input("Objectif de profit :")
            priorite = st.select_slider("Priorité", options=["Basse", "Standard", "Urgent 🔥", "CRITIQUE 💎"])
            submit = st.form_submit_button("Ajouter à la liste")
            
            if submit and nom:
                st.session_state.taches.append({
                    "nom": nom, 
                    "prio": priorite, 
                    "time": datetime.now().strftime("%H:%M")
                })
                st.rerun()

        for i, t in enumerate(st.session_state.taches):
            with st.expander(f"**[{t['prio']}]** {t['nom']}"):
                st.write(f"Inscrit à : {t['time']}")
                if st.button("Marquer comme terminé", key=f"fin_{i}"):
                    st.session_state.taches.pop(i)
                    st.balloons()
                    st.rerun()

    with col2:
        st.header("⏳ Turbo Focus")
        duree = st.select_slider("Session de travail (min)", options=[1, 15, 25, 45, 60, 90], value=25)
        
        if st.button("LANCER LE MODE PERFORMANCE"):
            sec = duree * 60
            progress_bar = st.progress(0)
            status = st.empty()
            
            for i in range(sec, -1, -1):
                m, s = divmod(i, 60)
                status.metric("CHRONO ELITE", f"{m:02d}:{s:02d}")
                progress_bar.progress(1 - (i / sec))
                time.sleep(1)
            
            st.success("SESSION TERMINÉE - REVENU ESTIMÉ : +100€")
            st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)

    with col3:
        st.header("🤖 Coach IA Expert")
        if len(st.session_state.taches) == 0:
            st.info("Aucune tâche active. Prêt pour un nouveau projet ?")
        elif len(st.session_state.taches) > 3:
            st.warning("⚠️ Trop d'objectifs ! Focus sur les priorités 'CRITIQUE' pour maximiser le ROI.")
        else:
            st.success("✅ Charge de travail optimale. Votre concentration est à son maximum.")

st.divider()
st.caption("© 2026 Neil Corporation - Solution logicielle de premier ordre")
