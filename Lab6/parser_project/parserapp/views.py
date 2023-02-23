from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request,"hello.html")

def twitter_data(request):
    return render(request,"twitter_scrape.html")