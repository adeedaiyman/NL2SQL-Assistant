from groq import Groq
import sqlparse

client = Groq(api_key="groq_api_key")

def generate_sql(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    # Remove markdown
    result = result.replace("```sql", "").replace("```", "").strip()

    # Ensure starts from SELECT
    if "SELECT" in result:
        result = result[result.find("SELECT"):]

    # 🔥 FORMAT SQL (THIS IS YOUR PART)
    result = sqlparse.format(result, reindent=True, keyword_case='upper')

    return result


# 🧠 Explain SQL
def explain_sql(sql_query):
    prompt = f"""
    Explain this SQL query in simple terms:

    {sql_query}

    Keep it short and easy to understand.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    # Clean output
    result = result.replace("```sql", "").replace("```", "").strip()

    # Force formatting (basic)
    if "SELECT" in result:
        result = result[result.find("SELECT"):]

    return result


# 📊 Auto Insights
def generate_insights(df):
    sample_data = df.head(10).to_string()

    prompt = f"""
    Analyze this dataset and provide 3-5 key insights:

    {sample_data}

    Keep insights short and business-focused.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    # Remove unwanted text
    if "SELECT" in result:
        result = result[result.find("SELECT"):]

    return result