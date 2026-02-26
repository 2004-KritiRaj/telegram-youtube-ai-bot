from services.transcript_service import fetch_transcript
from utils.youtube_utils import is_youtube_url, extract_video_id
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
from dotenv import load_dotenv

load_dotenv()


def start_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN not found in .env")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running. Waiting for messages...")
    app.run_polling()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi!\n\n"
        "Send me a YouTube link and I’ll summarize the video.\n\n"
        "🚀 Features coming next!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles incoming text messages.
    Detects YouTube links and fetches transcript.
    """
    message_text = update.message.text.strip()

    if is_youtube_url(message_text):
        video_id = extract_video_id(message_text)

        if not video_id:
            await update.message.reply_text(
                "❌ Unable to extract video ID.\nPlease send a valid YouTube link."
            )
            return

        await update.message.reply_text(
            "🎥 YouTube video detected!\n⏳ Fetching transcript..."
        )

        transcript = fetch_transcript(video_id)

        if not transcript:
            await update.message.reply_text(
                "❌ Transcript could not be retrieved for this video. This may be due to YouTube restrictions."
            )
            return

        await update.message.reply_text(
            "✅ Transcript fetched successfully!\n\n"
            f"📄 Transcript length: {len(transcript)} characters\n\n"
            "🧠 Ready to summarize next!"
        )

    else:
        await update.message.reply_text(
            "📎 Please send a valid YouTube video link."
        )