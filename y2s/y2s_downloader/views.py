from django.shortcuts import render
# pytube
from pytube import YouTube
import os


# Create your views here.

def y2s_down(request):
    return render(request, 'y2s main.html')


def y2s_download(request):
    global url
    url = request.GET.get('link')
    video = YouTube(url)


    video_stream = video.streams.filter(progressive=True).all()
    embd_link = url.replace('watch?v=', 'embed/')

    titles = video.title

    context = {'video': video_stream, "embed": embd_link, "titled": titles}



    return render(request, 'y2s download.html', context)


def yt_doanload_done(request,resolution) :
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method =="POST" :
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request,'done.html')
    else :
        return render(request , 'error.html')


