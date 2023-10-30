# import pytube
import pytube


url = input("Enter URL ~")
p = pytube.YouTube(url)
download_path = ('C://Users//conta//Desktop//YTDwn')
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.get_by_itag(135).download(download_path)
print('Done')

