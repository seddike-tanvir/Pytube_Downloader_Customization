# import pytube
from pytube import Playlist


url = input("Enter URL ~")
p = Playlist(url)
download_path = ('C://Users//conta//Desktop//YTDwn')
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.get_by_itag(140).download(download_path)
print('Done')

