# youtube_bot/utils/youtube_utils.py

import re


def is_youtube_url(text: str) -> bool:
    """
    Checks if the given text is a valid YouTube URL.
    Supports youtube.com and youtu.be links.
    """
    youtube_regex = (
        r"(https?://)?(www\.)?"
        r"(youtube\.com/watch\?v=|youtu\.be/)"
        r"[A-Za-z0-9_-]{11}"
    )
    return re.match(youtube_regex, text) is not None


def extract_video_id(url: str) -> str | None:
    """
    Extracts YouTube video ID from URL.
    Returns None if not found.
    """
    patterns = [
        r"v=([A-Za-z0-9_-]{11})",     # youtube.com/watch?v=ID
        r"youtu\.be/([A-Za-z0-9_-]{11})"  # youtu.be/ID
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None