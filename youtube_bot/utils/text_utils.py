# youtube_bot/utils/text_utils.py

import re
from typing import List


def clean_transcript(text: str) -> str:
    """
    Cleans raw transcript text.
    - Removes extra whitespace
    - Removes repeated line breaks
    - Normalizes spacing
    """
    if not text:
        return ""

    # Remove multiple newlines
    text = re.sub(r"\n+", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def chunk_text(text: str, max_words: int = 800) -> List[str]:
    """
    Splits text into chunks of max_words length.
    Used to handle long transcripts safely.
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks