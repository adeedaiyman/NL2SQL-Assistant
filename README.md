# 🤖 Conversational AI Data Analyst (NL2SQL Assistant)

An AI-powered data analysis tool that allows users to interact with structured datasets using natural language.  
Upload CSV files, ask questions in plain English, and get SQL queries, results, and visualizations instantly.

## 🚀 Features

- 💬 Chat-based interface (like ChatGPT)
- 📂 Upload multiple CSV files
- 🧠 Automatic schema detection
- 🔗 Smart JOIN detection across tables
- ⚡ Fast LLM responses (Groq API)
- 🧾 Clean formatted SQL generation
- 📊 Query execution with results table
- 📈 Auto visualization (charts)
- 📥 Download query results as CSV

## 🛠️ Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Groq API (LLM)
- sqlparse

## 🧠 How It Works

1. Upload one or more CSV files
2. Files are converted into SQL tables (SQLite)
3. User asks questions in natural language
4. LLM generates SQL queries
5. Queries are executed and results are displayed
6. Results can be visualized and downloaded

## Steps to create virtual environment
mkdir nl2sql-app
cd nl2sql-app
python3 -m venv venv
source venv/bin/activate
