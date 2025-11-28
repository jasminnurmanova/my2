from django.urls import path
from .views import car1,car2

urlpatterns=[
    path('car1/',car1),
    path('car2/', car2)
]