import streamlit as st
import time

st.set_page_config(page_title="Focus Dashboard", page_icon="🧠")

st.title("🚀 Dashboard Anti-Distraction")
st.write("Bienvenue Neil ! Prêt pour une session de travail intense ?")

# Barre latérale pour les réglages
st.sidebar.header("Réglages")
duree_minutes = st.sidebar.slider("Durée du Focus (minutes)", 1, 60, 25)

# Zone du minuteur
if st.button('Démarrer le Focus'):
    duree_secondes = duree_minutes * 60
    barre_progression = st.progress(0)
    affichage_temps = st.empty()
    
    for secondes in range(duree_secondes, -1, -1):
        mins, secs = divmod(secondes, 60)
        affichage_temps.metric("Temps restant", f"{mins:02d}:{secs:02d}")
        
        progression = 1 - (secondes / duree_secondes)
        barre_progression.progress(progression)
        
        time.sleep(1)
    
    st.balloons()
    st.success("🎉 Session terminée ! Prends une pause bien méritée.")
