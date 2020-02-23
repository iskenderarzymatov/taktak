from django.urls import path

from .views import *




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('deyatelnost/', DeyatelnostView.as_view(), name='deyatelnost'),
    path('news/', NewsView.as_view(), name='news'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('tours/', ToursView.as_view(), name='tours'),
    path('contactus/', ContactusView.as_view(), name='contactus'),


]