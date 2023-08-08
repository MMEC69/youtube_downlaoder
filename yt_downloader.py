from pytube import YouTube

def downloader(link):
    url = YouTube(link)
    video = url.streams.first()
    video.download()
