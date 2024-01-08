from django.urls import path

from covid.views import covidDetailsPageView, covidListPageView

urlpatterns = [
    path("covid/", covidListPageView, name="covid_list"),
    path("covid_details/", covidDetailsPageView, name="covid_details"),
]
