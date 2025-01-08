import threading
import asyncio
import time
from datetime import datetime, timedelta
from downloader.scraper import check_for_new_videos
from downloader.downloader import download_video, download_queue
from telegram_bot.bot import main as start_bot

def run_scraper():
    # Scrape all videos from yesterday on the first run
    yesterday = datetime.now() - timedelta(days=1)
    asyncio.run(check_for_new_videos('https://luciferdonghua.in', start_date=yesterday))

    # Continue scraping every 20 seconds
    while True:
        try:
            asyncio.run(check_for_new_videos('https://luciferdonghua.in'))
        except Exception as e:
            print(f"Error during scraping: {e}")
        time.sleep(20)  # Wait for 20 seconds before the next scraping cycle

if __name__ == '__main__':
    # Start the scraper in a separate thread
    scraper_thread = threading.Thread(target=run_scraper)
    scraper_thread.start()

    # Start the Telegram bot
    start_bot()
