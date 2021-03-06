from django.contrib import admin
from .models import Lists, TitleMovie


class ListsAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'private']
    # fieldsets = [

    # ]


class TitleMovieAdmin(admin.ModelAdmin):
    list_display = ['title_movie', 'user',
                    'watched', 'bookmark', 'date_added', 'movieDB_id']


admin.site.register(Lists, ListsAdmin)
admin.site.register(TitleMovie, TitleMovieAdmin)
