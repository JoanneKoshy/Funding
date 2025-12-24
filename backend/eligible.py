from backend.llm import ask_gemini


def check_eligibility(
    question: str,
    startup_age: float,
    sector: str,
    revenue_stage: str,
    state: str,
    language: str
) -> str:
    """
    Eligibility reasoning in ONE Gemini call (rate-limit safe)
    """

    prompt = f"""
    You are an AI startup funding advisor.

    Language to respond in: {language}

    STARTUP PROFILE:
    - Startup age: {startup_age} years
    - Sector: {sector}
    - Revenue stage: {revenue_stage}
    - State: {state}

    USER QUESTION:
    {question}

    TASK:
    1. Determine funding eligibility.
    2. Explain eligibility or ineligibility clearly.
    3. Suggest alternative schemes or next steps.

    Be practical, founder-friendly, and concise.
    """

    return ask_gemini(prompt)
