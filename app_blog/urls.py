from django.urls import path
from.views import indexView, inboxView, exploreView

urlpatterns = [
    path("index/", indexView, name="index"),
    path("contact/", inboxView, name="inbox"),
    path("exploreView/", exploreView, name="explore")

]
