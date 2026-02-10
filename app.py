import streamlit as st
import time
from datetime import datetime

# --- 1. CONFIGURATION DE LA PLATEFORME ---
st.set_page_config(
    page_title="PRO Focus AI - Suite Commerciale",
    page_icon="💎",
    layout="wide"
)

# --- 2. SÉCURITÉ DES DONNÉES (BOUTON RESET & NETTOYAGE) ---
if 'taches' not in st.session_state or not isinstance(st.session_state.taches, list):
    st.session_state.taches = []

# Sécurité pour les anciennes données (Nettoyage automatique)
if len(st.session_state.taches) > 0 and isinstance(st.session_state.taches[0], str):
    st.session_state.taches = []

# --- 3. BARRE LATÉRALE BUSINESS ---
with st.sidebar:
    st.title("💼 Neil Corp. Pro")
    menu = st.radio("Navigation", ["Tableau de Bord", "Devenir Membre PRO 💎"])
    st.divider()
    if st.button("⚠️ Réinitialiser l'App"):
        st.session_state.clear()
        st.rerun()

# --- 4. LOGIQUE DES PAGES ---

# --- PAGE ABONNEMENT ---
if menu == "Devenir Membre PRO 💎":
    st.title("📈 Maximisez vos Revenus")
    st.subheader("Choisissez la puissance de l'IA pour votre business")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("### Plan Standard\n**0€ / mois**\n\n- Accès au minuteur\n- Liste de tâches basique\n- Support communautaire")
        st.button("Votre plan actuel", disabled=True)
        
    with col_b:
        st.success("### Plan ELITE AI\n**19.99€ / mois**\n\n- Tâches Illimitées\n- Coach IA en temps réel\n- Alertes sonores premium\n- Rapports de productivité")
        if st.button("S'ABONNER MAINTENANT 🚀"):
            st.warning("Connexion sécurisée à Stripe en cours...")

# --- PAGE DASHBOARD ---
else:
    st.title("🚀 PRO Focus AI : Business Edition")
    st.write(f"Bienvenue Neil. Aujourd'hui est le {datetime.now().strftime('%d/%m/%Y')}")
    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.header("📋 Gestion de Projet")
        with st.form("form_tache"):
            nom = st.text_input("Objectif de profit :")
            priorite = st.select_slider("Priorité", options=["Basse", "Standard", "Urgent 🔥", "CRITIQUE 💎"])
            submit = st.form_submit_button("Ajouter à la liste")
            
            if submit and nom:
                st.session_state.taches.append({"nom": nom, "prio": priorite, "time": datetime.now().strftime("%H:%M")})
                st.rerun()

        for i, t in enumerate(st.session_state.taches):
            with st.expander(f"[{t['prio']}] {t['nom']}"):
                st.write(f"Inscrit à : {t['time']}")
                if st.button("Finaliser", key=f"fin_{i}"):
                    st.session_state.taches.pop(i)
                    st.balloons()
                    st.rerun()

    with col2:
        st.header("⚡ Turbo Focus")
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
            # Notification sonore HTML5
            st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)

    with col3:
        st.header("🤖 Coach IA Expert")
        if len(st.session_state.taches) == 0:
            st.write("Aucune tâche. L'IA attend vos ordres.")
        elif len(st.session_state.taches) > 3:
            st.error("⚠️ Alerte : Surcharge de travail détectée. Déléguez ou reportez.")
        else:
            st.success("✅ Rythme parfait. Vous êtes dans la zone de haute rentabilité.")

st.divider()
st.caption("© 2026 Neil Corporation - Solution logicielle de premier ordre")
