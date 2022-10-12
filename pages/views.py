from django.shortcuts import render

def Home(request):


    return render(request, 'pages/home.html')


def About(request):
    
    return render(request, 'pages/about.html')


