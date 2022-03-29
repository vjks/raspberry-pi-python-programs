from pytube import YouTube
link = "https://www.youtube.com/watch?v=fOGdb1CTu5c&t"
yt = YouTube( link )
yt.streams.get_highest_resolution().download()
