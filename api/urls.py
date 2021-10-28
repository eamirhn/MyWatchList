from django.urls import path, include
from .views import *
app_name = 'api'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('', apiTest, name='test'),
    path('all-movies/', movieList, name='all-movies'),
    path('create-movie/', movieCreate, name='create-movie'),
    path('movie-update/<int:movieDB_id>',
         movieUpdate, name='watched-update'),
    path('istheremovie/<int:movieDB_id>', isThereMovie, name='is-there-movie'),
    path('get-movie-by-moviedbid/<int:movieDB_id>',
         getMovieInfo, name='getMovieInfo')


]
