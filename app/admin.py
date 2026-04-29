from django.contrib import admin
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
    NewLetter
)

admin.site.register([
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
    NewLetter
])