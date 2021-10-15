from django.urls import path
from .views import *
urlpatterns = [
    path('',hospital, name='hospital'),
    path('doctor/',doctor, name='doctor'),
    path('mainDR/', main, name='MainDR'),
    path('nurse/',nurse, name='nurse'),
    path('patient/', patient, name='patient'),

]
