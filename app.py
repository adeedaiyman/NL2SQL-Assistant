import streamlit as st
import pandas as pd
import sqlite3
from sql_generator import generate_sql

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="AI Data Chat", layout="wide")

st.title("AI Data Chat Assistant")

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "schema_info" not in st.session_state:
    st.session_state.schema_info = ""

# -------------------------------
# Sidebar - Upload Files
# -------------------------------
st.sidebar.header("Upload Data")

uploaded_files = st.sidebar.file_uploader(
    "Upload CSV files",
    type=["csv"],
    accept_multiple_files=True
)

# DB connection
conn = sqlite3.connect("database.db")

# -------------------------------
# Load CSVs + Preview
# -------------------------------
if uploaded_files:
    schema_info = ""
    cursor = conn.cursor()

    st.subheader("Data Preview")

    for file in uploaded_files:
        df = pd.read_csv(file)

        table_name = file.name.replace(".csv", "")

        # Preview
        st.markdown(f"### {table_name}")
        st.dataframe(df.head(), use_container_width=True)

        # Save to DB
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        # Schema
        cursor.execute(f"PRAGMA table_info({table_name})")
        cols = [col[1] for col in cursor.fetchall()]
        schema_info += f"Table: {table_name}\nColumns: {', '.join(cols)}\n\n"

    st.session_state.schema_info = schema_info
    st.sidebar.success("Data loaded successfully!")

# -------------------------------
# Show Chat History
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask about your data...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # -------------------------------
    # Prompt
    # -------------------------------
    prompt = f"""
    You are an expert SQL generator.

    Database schema:
    {st.session_state.schema_info}

    Rules:
    - Return ONLY SQL query
    - Format SQL in clean multi-line format
    - Use proper indentation
    - Each clause on new line (SELECT, FROM, JOIN, WHERE, GROUP BY, ORDER BY)
    - Do NOT return explanation
    - Do NOT return multiple queries
    - Use JOIN when needed
    - Use valid SQLite syntax

    Example format:

    SELECT column1, column2
    FROM table_name
    JOIN other_table ON condition
    WHERE condition
    GROUP BY column1
    ORDER BY column1;

    Question:
    {user_input}
    """

    # -------------------------------
    # Generate SQL
    # -------------------------------
    sql_query = generate_sql(prompt)

    # -------------------------------
    # Execute SQL
    # -------------------------------
    try:
        result = pd.read_sql_query(sql_query, conn)

        response = f"**SQL Query:**\n```sql\n{sql_query}\n```"

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.markdown(response)
            st.dataframe(result, use_container_width=True)

    except:
        # fallback if not SQL
        st.session_state.messages.append({
            "role": "assistant",
            "content": sql_query
        })

        with st.chat_message("assistant"):
            st.markdown(sql_query)