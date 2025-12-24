from backend.rag import retrieve_context_by_state

query = "What funding support is available for startups?"
state = "Kerala"

context = retrieve_context_by_state(query, state)
print(context)
