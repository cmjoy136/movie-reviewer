from django.urls import path
from django.contrib import admin
from movie_reviewer.reviews import views

urlpatterns = [

# path('', views.index, name='homepage'),
path('review/<int:id>', views.review_view),
path('reviewadd/', views.reviewaddview),




 ]

