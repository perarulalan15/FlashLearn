from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flashcards', views.flashcards_view, name='flashlearnapp'),  # Flashcards view at /flashcards/
    path('signup', views.signup, name='signup'),  # Signup view at /signup/
    path('signin', views.signin, name='signin'),  # Signin view at /signin/
]
