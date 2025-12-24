from backend.rag import answer_with_rag

question = "What funding support is available for early-stage startups?"
answer = answer_with_rag(question)

print(answer)
