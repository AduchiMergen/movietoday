from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from taggit.managers import TaggableManager


def _(x):
    return x


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name = _('Cinema')
        verbose_name_plural = _('Cinemas')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    cinema = models.ForeignKey('cinema.Cinema')
    movie = models.ForeignKey('cinema.Movie')
    date = models.DateField()

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')

    def __str__(self):
        return '%s %s' % (self.cinema, self.date)


class MovieInCinema(models.Model):
    movie = models.ForeignKey('cinema.Movie')
    cinema = models.ForeignKey('cinema.Cinema')
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    filmbase_id = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = TaggableManager()

    def __str__(self):
        return self.title


class Poster(models.Model):
    movie = models.ForeignKey('cinema.Movie')
    url = models.URLField()


@receiver(post_migrate)
def init_cinemas(sender, **kwargs):
    Cinema.objects.get_or_create(name='goodwin', defaults={'url': 'http://goodwincinema.ru'})
    Cinema.objects.get_or_create(name='kino-polis', defaults={'url': 'http://kino-polis.ru'})
    Cinema.objects.get_or_create(name='kinomir', defaults={'url': 'http://kinomir.tom.ru'})
