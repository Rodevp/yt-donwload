from pytube import YouTube
from sys import argv

def main() :

    link = argv[1]
    yt = YouTube(link)

    print("----INFO VIDEO----")
    print(f"{yt.title} - {yt.views} - {yt.author}")

    youtube_download = yt.streams.get_highest_resolution()

    youtube_download.download("./videos")



if __name__ == "__main__" :
    main()