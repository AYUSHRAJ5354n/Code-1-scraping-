import threading
import asyncio
from downloader.scraper import check_for_new_videos
from downloader.downloader import download_video, download_queue
from telegram_bot.bot import main as start_bot

def run_scraper():
    asyncio.run(check_for_new_videos('https://luciferdonghua.in'))  # Replace 'https://example.com' with your target website URL

if __name__ == '__main__':
    # Start the scraper in a separate thread
    scraper_thread = threading.Thread(target=run_scraper)
    scraper_thread.start()

    # Start the Telegram bot
    start_bot()
