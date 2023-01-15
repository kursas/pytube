from pytube import YouTube
link_list =['https://www.youtube.com/watch?v=GKSRyLdjsPA','https://www.youtube.com/watch?v=AUvodoVurps']
for link in link_list:
    url = YouTube(str(link))
    audio = url.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download(r'D:/DUMENYS/DARIUS/Desktop')
#output
Process finished with exit code 0
