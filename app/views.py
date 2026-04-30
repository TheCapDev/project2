from datetime import date

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_POST

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
  NewsLetter,
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
    "newsLetter": NewsLetter.objects.all(),
    }
  template = loader.get_template("news.html")
  return HttpResponse(template.render(context, request))


@require_POST
def subscribe_newsletter(request):
  email = (request.POST.get("email") or "").strip()
  redirect_to = request.META.get("HTTP_REFERER") or reverse("index")

  try:
    validate_email(email)
  except ValidationError:
    messages.error(request, "Please enter a valid email address.")
    return HttpResponseRedirect(redirect_to)

  if NewsLetter.objects.filter(email__iexact=email).exists():
    messages.info(request, "You're already subscribed to our newsletter.")
  else:
    NewsLetter.objects.create(email=email, date=date.today(), active=True)
    messages.success(request, "Thanks for subscribing!")

  return HttpResponseRedirect(redirect_to)
