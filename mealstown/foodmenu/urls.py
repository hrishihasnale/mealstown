from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    cuisineMain
)


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('cuisine_list/', cuisineMain.UserRegister.as_view()),
    path('cuisine_items/<?cuisine_id>', cuisineMain.UserLogin.as_view()),
    path('cuisine_search/', cuisineMain.UserRegister.as_view()),
    path('best_sellers/items/', cuisineMain.UserRegister.as_view()),
]