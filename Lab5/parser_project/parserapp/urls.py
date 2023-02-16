from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('twitter_scrape/',views.twitter_data)

]