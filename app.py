import streamlit as st
import time

st.set_page_config(page_title="Focus Dashboard", page_icon="🧠")

st.title("🚀 Dashboard Anti-Distraction")

# --- SECTION 1 : TO-DO LIST (Mémoire) ---
st.subheader("✅ Mes Tâches Prioritaires")

if 'taches' not in st.session_state:
    st.session_state.taches = []

nouvelle_tache = st.text_input("Ajoute une tâche importante et appuie sur Entrée :")
if nouvelle_tache:
    if nouvelle_tache not in st.session_state.taches:
        st.session_state.taches.append(nouvelle_tache)

for i, tache in enumerate(st.session_state.taches):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"🔹 {tache}")
    if col2.button("Fait", key=f"btn_{i}"):
        st.session_state.taches.pop(i)
        st.rerun()

st.divider()

# --- SECTION 2 : MINUTEUR ---
st.subheader("⏳ Mode Focus")
duree_min = st.sidebar.slider("Minutes", 1, 60, 25)

if st.button('Démarrer le Focus'):
    duree_sec = duree_min * 60
    affichage = st.empty()
    barre = st.progress(0)
    for s in range(duree_sec, -1, -1):
        m, sec = divmod(s, 60)
        affichage.metric("Temps restant", f"{m:02d}:{sec:02d}")
        barre.progress(1 - (s / duree_sec))
        time.sleep(1)
    st.balloons()
