import pafy
import sys

def  main(video_source):

    url = video_source
    video = pafy.new(url) 
  
    streams = video.streams

    # get best resolution regardless of format 
    best = video.getbest() 
    #bestaudio = video.getbestaudio()
    best.download(filepath="./video/")



if __name__ == "__main__":
    if len(sys.argv) == 2:
        video_source = sys.argv[1]
        main(video_source)
    else:
        print('Nie podano pliku video!')
        print ('\n')
