from django.urls import path

from . import views
from .views import redirect_url_view

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:urlHash>', redirect_url_view, name='redirect'),
]
