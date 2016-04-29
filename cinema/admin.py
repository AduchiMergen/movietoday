from django.contrib import admin

from cinema.models import Cinema, Schedule, MovieInCinema, Movie, Poster

admin.site.register(Cinema)


class MovieInCinemaAdmin(admin.ModelAdmin):
    list_display = ['movie', 'cinema', 'duration', 'filmbase_id']
    list_filter = ['cinema', 'movie']


class PosterAdmin(admin.ModelAdmin):
    list_display = ['movie', 'url']
    list_filter = ['movie']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['movie', 'cinema', 'date']
    list_filter = ['movie', 'cinema']
    date_hierarchy = 'date'


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['genre']

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieInCinema, MovieInCinemaAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Schedule, ScheduleAdmin)
