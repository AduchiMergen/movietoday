from datetime import timedelta, datetime

import requests
from cinema.forms import MovieInCinemaForm
from cinema.models import Cinema, Movie, MovieInCinema, Schedule, Poster
from django.utils import timezone


def check_schedules():
    for cinema in Cinema.objects.all():
        check_schedule(cinema)


def save_film(movie_data):
    movie, _ = Movie.objects.get_or_create(title=movie_data['title'])
    movie.genre.add(*movie_data['genre'].split(', '))
    return movie


def save_poster(movie, poster_url):
    poster, _ = Poster.objects.get_or_create(movie=movie, url=poster_url)
    return poster


def save_movie_in_cinema(cinema, movie, movie_data):
    try:
        instance = MovieInCinema.objects.get(cinema=cinema, movie=movie)
    except MovieInCinema.DoesNotExist:
        instance = MovieInCinema(cinema=cinema, movie=movie)
    form = MovieInCinemaForm(instance=instance, data=movie_data)
    if form.is_valid():
        return form.save()
    else:
        print(form.errors)
        return None


def save_schedule(cinema, movie, date):
    schedule, _ = Schedule.objects.get_or_create(movie=movie, cinema=cinema, date=date)
    return schedule


def parse_schedule_data(cinema, data):
    date = datetime.strptime(data['date'], '%d.%m.%Y')
    for movie_data in data.get('films', []):
        movie = save_film(movie_data)
        poster = save_poster(movie, cinema.url + movie_data['preview'])
        movie_in_cinema = save_movie_in_cinema(cinema, movie, movie_data)
        schedule = save_schedule(cinema, movie, date)


def check_schedule(cinema):
    print('Check schedule for {name} cinema.'.format(name=cinema.name))
    url = '{host}/schedule/'.format(host=cinema.url)
    today = timezone.localtime(timezone.now()).date()

    for day_delta in range(14):
        schedule_day = today + timedelta(days=day_delta)

        schedule_day_str = schedule_day.strftime('%d.%m.%Y')
        params = {'ajax': 1, 'date': schedule_day_str}

        response = requests.get(url, params)
        schedule_json = response.json()
        if schedule_json.get('hasSeancesForSale', 0):
            parse_schedule_data(cinema, schedule_json)
            print(' - {date} schedule saved'.format(date=schedule_day_str))
        else:
            print(' - {date} schedule empty'.format(date=schedule_day_str))
            break
