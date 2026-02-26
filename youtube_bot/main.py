# youtube_bot/main.py

from bot.telegram_bot import start_bot


def main():
    """
    Application entry point.
    Starts the Telegram bot.
    """
    print("🚀 Starting Telegram YouTube AI Bot...")
    start_bot()


if __name__ == "__main__":
    main()