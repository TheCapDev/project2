from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import (
  Slider,
  Advertisement,
  SocialLink,
  Celebrity,
  Trailer,
  TrailerItem,
  News,
  Tweet,
  MovieTheater,
  MovieTv,
  NewLetter,
)


def index(request):
  context = {
    "slider": Slider.objects.all(),
    "advertisement_sidebar": Advertisement.objects.filter(section="sidebar"),
    "advertisement_latestNew": Advertisement.objects.filter(section="latestNew"),
    "socialLink": SocialLink.objects.all(),
    "celebrity": Celebrity.objects.all(),
    "trailer": Trailer.objects.all(),
    "trailerItem": TrailerItem.objects.all(),
    "news_image": News.objects.filter(section="image"),
    "news_blog": News.objects.filter(section="blog"),
    "news_left": News.objects.filter(section="left"),
    "news_right": News.objects.filter(section="right"),
    "tweet": Tweet.objects.all(),
    "movieTheater_popular": MovieTheater.objects.filter(type="popular"),
    "movieTheater_coming_soon": MovieTheater.objects.filter(type="coming_soon"),
    "movieTheater_top_rated": MovieTheater.objects.filter(type="top_rated"),
    "movieTheater_most_reviewed": MovieTheater.objects.filter(type="most_reviewed"),
    "movieTv_popular": MovieTv.objects.filter(type="popular"),
    "movieTv_coming_soon": MovieTv.objects.filter(type="coming_soon"),
    "movieTv_top_rated": MovieTv.objects.filter(type="top_rated"),
    "movieTv_most_reviewed": MovieTv.objects.filter(type="most_reviewed"),
    "newLetter": NewLetter.objects.all(),
    }
  template = loader.get_template("news.html")
  return HttpResponse(template.render(context, request))
