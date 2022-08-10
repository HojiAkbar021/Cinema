from django.contrib import admin
from movies.models import Actor, Category, Genre, Movie, MovieShots, Rating, RatingStar, Reviews, Setting

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Setting)