from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def result(request):
    print("Got Post Info....................")
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        "name" : name,
    "location" : location,
    "language" : language,
    "comment" : comment,
    }
    return render(request,"result.html",context)

#this is not working because the previous method is not redirecting to "/success"
def success(request):
    return render(request,"success.html")