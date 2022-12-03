from pytube import YouTube
from sys import argv

def main() :
    link = argv[1]
    yt = YouTube(link)

    print(yt.title)



if __name__ == "__main__" :
    main()