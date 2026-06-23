import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from core.rag import ask
import pandas as pd

# -----------------------------
# TABLE RENDERING
# -----------------------------
def render_table(text):
    lines = text.split("\n")

    table_lines = [
        line.strip()
        for line in lines
        if "|" in line and line.strip()
    ]

    if len(table_lines) < 3:
        return False

    try:
        rows = []

        for line in table_lines:
            cells = [c.strip() for c in line.split("|")]

            if cells and cells[0] == "":
                cells = cells[1:]
            if cells and cells[-1] == "":
                cells = cells[:-1]

            rows.append(cells)

        header = rows[0]
        data = rows[2:]  # skip markdown separator row

        df = pd.DataFrame(data, columns=header)

        st.table(df)
        return True

    except Exception:
        return False


# -----------------------------
# UI CONFIG
# -----------------------------
st.set_page_config(page_title="ML Tutor RAG", layout="wide")

st.title("🧠 Machine Learning Tutor (RAG System)")


# -----------------------------
# SESSION STATE
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []


# -----------------------------
# INPUT
# -----------------------------
user_input = st.text_input("Ask a Machine Learning question:")

if user_input:
    answer = ask(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Tutor", answer))


# -----------------------------
# CHAT RENDER
# -----------------------------
for role, msg in st.session_state.chat:

    if role == "You":
        st.markdown(f"### 🧑 You")
        st.write(msg)

    else:
        st.markdown(f"### 🧠 Tutor")

        # Try table rendering first
        if not render_table(msg):
            st.write(msg)