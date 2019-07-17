from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d %Y", localtime()),
        "date": strftime("%m-%d-%Y %H:%M %p", localtime())

    }
    return render(request,'first_app/index.html', context)
