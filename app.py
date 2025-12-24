import streamlit as st
from backend.rag import retrieve_context_by_state
from backend.eligible import check_eligibility
@st.cache_data(show_spinner=False)
def cached_gemini_response(prompt):
    return ask_gemini(prompt)

from backend.rag import answer_with_rag

from backend.llm import ask_gemini
from backend.language import (
    translate_to_english,
    translate_from_english
)



# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Funding AI",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🇮🇳 Multilingual Funding Intelligence System")
st.caption("AI-powered funding, investor & policy intelligence for founders")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🧠 Features")

feature = st.sidebar.radio(
    "Choose a feature",
    (
        "Eligibility Check",
        "Regional Funding",
        "Funding Trends",
        "Policy Simplifier",
        "Investor Interest",
        "Common Rejection Reasons"
    )
)

st.sidebar.markdown("---")

st.sidebar.header("🌐 Language")
language = st.sidebar.selectbox(
    "Select language",
    ("English", "Malayalam", "Hindi")
)

# ---------------- MAIN AREA ----------------
st.subheader(f"🔍 {feature}")

# ---- FEATURE-SPECIFIC INPUTS ----

# Eligibility Check inputs
if feature == "Eligibility Check":
    col1, col2 = st.columns(2)
    with col1:
        startup_age = st.number_input("Startup age (years)", min_value=0.0, step=0.1)
        sector = st.text_input("Sector (e.g., Agritech, Fintech)")
    with col2:
        revenue_stage = st.selectbox(
            "Revenue stage",
            ("Pre-revenue", "Early revenue", "Growing revenue")
        )
        state = st.text_input("State")

# Regional Funding inputs
elif feature == "Regional Funding":
    state = st.text_input("Enter your state")

# Policy Simplifier inputs
elif feature == "Policy Simplifier":
    uploaded_file = st.file_uploader(
        "Upload policy document (PDF)",
        type=["pdf"]
    )

# Funding Trends / Investor features / Rejection reasons
question = st.text_area(
    "Ask your question",
    placeholder="Type your question here..."
)

submit = st.button("Submit")

# ---------------- DEBUG OUTPUT (TEMPORARY) ----------------
# ---------------- SUBMIT HANDLER ----------------
# ---------------- SUBMIT HANDLER ----------------
# ---------------- SUBMIT HANDLER ----------------
if submit:
    st.markdown("### 🤖 AI Response")

    # 1️⃣ Translate user input → English
    normalized_question = translate_to_english(question, language)

    
    if feature == "Regional Funding":
        context = retrieve_context_by_state(normalized_question, state)

        prompt = f"""
You are an AI assistant for regional startup funding intelligence.

Use the provided context as the primary source.
If the context does not fully answer the question, you may:
- Use your general knowledge about Indian startup funding
- Clearly state that the response is based on general insights
- Provide best-possible guidance instead of refusing
- do not keep it too long, make it optimzed and good soo that a founder can read it quickly and in a positive way as if, it is available and really good and no need of validition at start, just start with points

CONTEXT:
{context}

QUESTION:
{normalized_question}

Respond clearly, practically, and founder-friendly.
"""


        english_answer = ask_gemini(prompt)

    else:
        english_answer = answer_with_rag(normalized_question)

    # 3️⃣ Translate back to selected language
    final_answer = translate_from_english(english_answer, language)



    if feature == "Eligibility Check":
        english_answer = check_eligibility(
        question=normalized_question,
        startup_age=startup_age,
        sector=sector,
        revenue_stage=revenue_stage,
        state=state,
        language=language
    )

    # 4️⃣ Display answer
    st.write(final_answer)

    # ---- Debug Info (optional) ----
    with st.expander("🔧 Debug Info"):
        st.write("Feature:", feature)
        st.write("Language:", language)
        st.write("Original Question:", question)
        st.write("Normalized (English):", normalized_question)

        if feature == "Eligibility Check":
            st.write({
                "Startup Age": startup_age,
                "Sector": sector,
                "Revenue Stage": revenue_stage,
                "State": state
            })

        if feature == "Policy Simplifier":
            st.write("Uploaded file:", uploaded_file.name if uploaded_file else "No file")
