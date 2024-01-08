
from django.urls import path
from vsview.views import AboutPageView, HomePageView, plipListPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('plip', plipListPageView, name='plip_list'),

    path('about/', AboutPageView.as_view(), name='about')
]
