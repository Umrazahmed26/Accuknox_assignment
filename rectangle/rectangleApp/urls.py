from django.urls import path, include
from . import views

urlpatterns = [
    path('test_rectangle/', views.test_rectangle, name='test_rectangle'),

    

]