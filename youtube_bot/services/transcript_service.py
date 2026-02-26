from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable


def fetch_transcript(video_id: str) -> str | None:
    """
    Fetch transcript for a YouTube video.
    Tries all available transcripts and skips broken ones.
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        for transcript in transcript_list:
            try:
                data = transcript.fetch()
                text = " ".join(item["text"] for item in data)
                if text.strip():
                    return text
            except Exception:
                # Skip broken / blocked transcripts
                continue

        return None

    except (TranscriptsDisabled, VideoUnavailable):
        return None
    except Exception:
        return None