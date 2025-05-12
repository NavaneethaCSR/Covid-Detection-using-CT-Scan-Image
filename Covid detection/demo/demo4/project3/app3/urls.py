
from django.urls import path

from . import views

urlpatterns = [
  path('', views.signinfun, name='signin'),
  path('signup', views.signupfun, name='signup'),
  path('signin', views.signinfun, name='signin'),
  path('upload', views.uploadfun, name='upload'),
  path('upload#', views.signinfun, name='signin'),

path('pastpred', views.statusfun, name='pastpred'),
# path('history', views.predictfun, name='history'),
]