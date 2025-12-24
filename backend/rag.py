import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = "data/policies"
VECTOR_DB_DIR = "vector_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def ingest_documents():
    documents = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):

            # 👇 VERY IMPORTANT: Infer state from filename
            filename = file.lower()

            if "kerala" in filename:
                state = "Kerala"
                scheme_type = "State"
            elif "karnataka" in filename:
                state = "Karnataka"
                scheme_type = "State"
            else:
                state = "Central"
                scheme_type = "Central"

            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            docs = loader.load()

            for doc in docs:
                doc.metadata["state"] = state
                doc.metadata["type"] = scheme_type

            documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    vectordb.persist()
    return vectordb



def load_vector_db():
    return Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )


def retrieve_context(query, k=4):
    db = load_vector_db()
    results = db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])

from backend.llm import ask_gemini


def answer_with_rag(question: str) -> str:
    """
    Uses retrieved document context + Gemini to generate grounded answer
    """
    context = retrieve_context(question)

    prompt = f"""
    You are an AI assistant for startup funding and policy intelligence.
    Answer ONLY using the context provided below.
    If the answer is not present, say you do not have enough information.

    --- CONTEXT ---
    {context}

    --- QUESTION ---
    {question}

    Answer clearly and concisely.
    """

    return ask_gemini(prompt)


def retrieve_context_by_state(query, state, k=4):
    db = load_vector_db()

    # 1️⃣ Try state-specific schemes
    state_results = db.similarity_search(
        query,
        k=k,
        filter={"state": state}
    )

    # 2️⃣ If not enough, fall back to central schemes
    if len(state_results) < k:
        central_results = db.similarity_search(
            query,
            k=k - len(state_results),
            filter={"type": "Central"}
        )
        state_results.extend(central_results)

    return "\n".join([doc.page_content for doc in state_results])

