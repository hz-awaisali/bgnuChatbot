from django.urls import path
from .views import AskBot

urlpatterns = [
    path("ask/", AskBot.as_view())
]
