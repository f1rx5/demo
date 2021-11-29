from django.urls import path
from . import views
urlpatterns=[
    path('registration/', views.fnreg, name='registration'),
    path('sample/',views.fnsample, name='sample'),
    ]