from backend.eligible import check_eligibility

answer = check_eligibility(
    question="Am I eligible for funding?",
    startup_age=1.5,
    sector="Fintech",
    revenue_stage="Pre-revenue",
    state="Kerala"
)

print(answer)
