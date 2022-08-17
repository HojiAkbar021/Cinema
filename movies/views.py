from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from movies.models import Setting, Movie, Category


def settings(request):
    setting = Setting.objects.latest('id')
    movie = Movie.objects.get()
    context = {
        'setting' : setting,
        'movie' : movie
    }
    return render(request, 'index.html', context)


def movie_create(request):
    setting= Setting.objects.latest('description')
    category= Category.objects.all()
    if request.method == "POST":
        title= request.POST.get('title')
        tagline= request.POST.get('tagline')
        description= request.POST.get('description')
        poster= request.FILES.get('poster')
        year= request.POST.get('year')
        country= request.POST.get('country')
        directors= request.POST.get('directors')
        actors= request.POST.get('actors')
        genres= request.POST.get('genres')
        world_premiere= request.POST.get('world_premiere')
        budget= request.POST.get('budget')
        fees_in_usa= request.POST.get('fees_in_usa')
        fees_in_world= request.POST.get('fess_in_world')
        category= request.POST.get('category')
        movie= Movie.objects.create(
                                    title= title, 
                                    tagline= tagline,
                                    description= description, 
                                    poster= poster,
                                    year= year,
                                    country= country,
                                        directors= directors,
                                        actors= actors,
                                        genres= genres,
                                        world_premiere=world_premiere,
                                        budget= budget,
                                        fees_in_usa= fees_in_usa,
                                        fees_in_world= fees_in_world,
                                        category= category,
                                    )
        return redirect('index')
    context= {
        'setting': setting,
        'category': category,
    }
    return render(request, 'index.html', context)

def movie_detail(request, id):
    movie = Movie.objects.get(id = id)
    setting = Setting.latest('id')
    context = {
        'setting' : setting,
        'movie' : movie
    }
    return render(request, 'movie_page-fuul.html', context) 


def movie_update(request, id):
    setting= Setting.objects.latest('id')
    movie= Movie.objects.get(id=id)
    category=Category.objects.all()
    if request.method == "POST":
        try:
            title= request.POST.get('title')
            tagline= request.POST.get('tagline')
            description= request.POST.get('description')
            poster= request.FILES.get('poster')
            year= request.POST.get('year')
            country= request.POST.get('country')
            directors= request.POST.get('directors')
            actors= request.POST.get('actors')
            genres= request.POST.get('genres')
            world_premiere= request.POST.get('world_premiere')
            budget= request.POST.get('budget')
            fees_in_usa= request.POST.get('fees_in_usa')
            fees_in_world= request.POST.get('fess_in_world')
            category= request.POST.get('category')
            movie= Movie.objects.get(id = id)
            movie.title = title
            movie.tagline = tagline
            movie.description = description
            movie.poster = poster
            movie.year = year
            movie.country = country
            movie.directors = directors
            movie.actors = actors
            movie.genres = genres
            movie.world_premiere = world_premiere
            movie.budget = budget
            movie.fees_in_usa = fees_in_usa
            movie.fees_in_world = fees_in_world
            movie.category = category   
            movie.save()
            return redirect('index', movie.id)

        except:
                return HttpResponse('Error')
    context={
        'setting': setting,
        'movie': movie,
        'category': category,
    }
    return render(request, 'index.html', context)

def movie_delete(request,id):
    setting= Setting.objects.latest('id')
    movie= Movie.objects.get(id= id)
    if request.method == "POST":
        movie= Movie.objects.get(id= id)
        movie.delete()
        return redirect('index')
    context= {
        'setting': setting,
        'movie': movie,
    }
    return render(request, 'index.html', context)

