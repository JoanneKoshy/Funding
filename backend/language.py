from backend.llm import ask_gemini


LANGUAGE_MAP = {
    "English": "English",
    "Malayalam": "Malayalam",
    "Hindi": "Hindi"
}


def translate_to_english(text: str, source_language: str) -> str:
    """
    Translates user input to English if needed
    """
    if source_language == "English":
        return text

    prompt = f"""
    Translate the following text from {source_language} to English.
    Only return the translated text.

    Text:
    {text}
    """
    return ask_gemini(prompt)


def translate_from_english(text: str, target_language: str) -> str:
    """
    Translates English output to target language if needed
    """
    if target_language == "English":
        return text

    prompt = f"""
    Translate the following text from English to {target_language}.
    Keep it clear and natural.

    Text:
    {text}
    """
    return ask_gemini(prompt)
