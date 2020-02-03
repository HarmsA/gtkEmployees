from django.urls import path
from pages import views

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('view_all', views.View_all, name='view_all'),
    path('view_quiz', views.View_quiz, name='view_quiz'),
    path('view_bio/', views.View_bio, name='view_bio'),
    path('change_bio/', views.Change_bio, name='change_bio'),
    path('about/', AboutPageView.as_view(), name='about'),
]
