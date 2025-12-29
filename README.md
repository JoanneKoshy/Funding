# Funding Expert

**Funding Expert** is a **Multilingual AI-powered Funding Intelligence System** that helps startup founders discover funding opportunities, understand eligibility, analyze investor expectations, simplify policy documents, and track funding trends — all through a conversational interface in **English, Malayalam, and Hindi**.

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Tech stack](#tech-stack)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Install](#install)
  * [Configuration](#configuration)
  * [Running](#running)
* [Usage](#usage)
* [Testing](#testing)
* [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

---

## About

Accessing startup funding information in India is fragmented across policy PDFs, reports, portals, and announcements — often available only in English and difficult to interpret.

**Funding** solves this by providing a **Retrieval-Augmented Generation (RAG)–based AI system** that:

* Retrieves relevant funding and policy information from documents
* Applies intelligent reasoning when data is incomplete
* Explains insights in a **founder-friendly and multilingual** manner

The system is designed for:

* Early-stage founders
* Student entrepreneurs
* Startup ecosystem participants
* Incubators and innovation cells

---

## Features

* **Eligibility Check (Reasoning Engine)**
  Evaluates startup eligibility for funding based on sector, stage, age, and location using intelligent LLM reasoning (no hard refusals).

* **Regional Funding Discovery (RAG + LLM fallback)**
  Retrieves state-specific funding schemes and supplements missing information with informed AI reasoning.

* **Funding Trends Analysis (Hybrid RAG)**
  Analyzes funding trend reports and market documents to surface sector-wise and stage-wise funding patterns.

* **Policy Simplifier (Per-upload RAG)**
  Upload government or institutional policy PDFs and receive simplified, founder-friendly explanations grounded in actual clauses.

* **Investor Interest Analysis**
  Simulates investor expectations based on startup profile (sector, stage, geography).

* **Common Rejection Reasons**
  Identifies common investor rejection patterns and provides actionable improvement suggestions.

* **Full Multilingual UI & Responses**
  Entire interface and AI responses dynamically switch between **English, Malayalam, and Hindi**.

---

## Tech stack

* **Frontend & App Framework**: Streamlit
* **LLM**: Google Gemini API
* **RAG Framework**: LangChain
* **Vector Database**: ChromaDB
* **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **Document Parsing**: PyPDF
* **Language Translation**: LLM-based translation pipeline
* **Environment**: Python 3.10+, Conda

---

## Getting Started

### Prerequisites

* Python >= 3.10
* Conda / Miniconda
* Git
* Google Gemini API key

---

### Install

1. Clone the repository:

```bash
git clone https://github.com/JoanneKoshy/Funding.git
cd Funding
```

2. Create and activate a Conda environment:

```bash
conda create -n funding_ai python=3.10 -y
conda activate funding_ai
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Configuration

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

Ensure the environment variable is loaded before running the app.

---

### Running

Start the Streamlit app:

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Usage

### Example workflows

* **Eligibility Check**

  * Input startup age, sector, revenue stage, and state
  * Receive eligibility reasoning and funding readiness insights

* **Regional Funding**

  * Ask state-specific funding questions
  * Retrieve grounded schemes with AI fallback reasoning

* **Policy Simplifier**

  * Upload a funding or government policy PDF
  * Ask questions like:

    * “Explain this policy in simple terms”
    * “What does this mean for early-stage startups?”

* **Funding Trends**

  * Ask trend-based questions such as:

    * “Which sectors are receiving the most funding in India?”
    * “What should early-stage startups prepare for?”

* **Investor Intelligence**

  * Analyze investor interest and rejection reasons based on startup profile

---

## Testing

Manual testing is supported via the Streamlit UI.

For future improvements:

* Unit tests can be added for RAG pipelines
* Mock LLM responses for deterministic testing
* Automated document ingestion tests

---

## Deployment

Deployment options include:

* **Streamlit Cloud**
* **Render**
* **Vercel (via Streamlit container)**
* **Docker (recommended for reproducibility)**

Basic Docker flow:

```bash
docker build -t funding-ai .
docker run -p 8501:8501 funding-ai
```

---

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit changes with clear messages
4. Open a pull request with a description

Please ensure code quality and clarity before submitting.

---

## License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

* Google Gemini API
* LangChain
* ChromaDB
* Sentence Transformers
* Streamlit Community

---

## Contact

**Maintainer:** Joanne Koshy
**GitHub:** [@JoanneKoshy](https://github.com/JoanneKoshy)
**Repository:** [https://github.com/JoanneKoshy/Funding](https://github.com/JoanneKoshy/Funding)

---
