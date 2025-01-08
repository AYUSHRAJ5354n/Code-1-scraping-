import yt_dlp
import queue
import threading

download_queue = queue.Queue()

def download_worker():
    while True:
        url = download_queue.get()
        if url is None:
            break
        download_video(url)
        download_queue.task_done()

def download_video(url):
    ydl_opts = {
        'format': 'best[height<=480]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Start worker thread
threading.Thread(target=download_worker, daemon=True).start()
