# youtube_bot/services/summary_service.py

from typing import Dict, List
from youtube_bot.utils.text_utils import clean_transcript, chunk_text

def generate_summary(transcript: str) -> Dict[str, List[str] | str]:
    """
    Generates a structured summary from transcript text.

    NOTE:
    This is a placeholder implementation.
    It will later be replaced with LLM / OpenClaw logic.
    """

    if not transcript:
        return {
            "key_points": [],
            "timestamps": [],
            "takeaway": "Transcript not available."
        }

    # Step 1: Clean transcript
    cleaned_text = clean_transcript(transcript)

    # Step 2: Chunk transcript
    chunks = chunk_text(cleaned_text)

    # Step 3: Dummy summarization logic (for now)
    # We simulate "key points" by taking first lines of chunks
    key_points = []
    for chunk in chunks[:5]:  # limit to 5 points
        words = chunk.split()
        point = " ".join(words[:20]) + "..."
        key_points.append(point)

    # Step 4: Dummy timestamps (placeholder)
    timestamps = [
        "00:00 – Introduction",
        "05:00 – Main discussion",
        "10:00 – Key explanation",
    ]

    # Step 5: Dummy core takeaway
    takeaway = (
        "This video explains the main concepts step by step "
        "and highlights the most important ideas clearly."
    )

    return {
        "key_points": key_points,
        "timestamps": timestamps,
        "takeaway": takeaway
    }