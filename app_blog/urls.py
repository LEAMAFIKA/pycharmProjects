from django.urls import path
from.views import indexView, inboxView, exploreView

urlpatterns = [
    path("", indexView, name="index"),
    path("contact/", inboxView, name="inbox"),
    path("exploreView/", exploreView, name="explore")

]
