from django.urls import path
from .views import home_view, root_view_page, portfolio

urlpatterns = [
    path("home/", home_view),
    path("", root_view_page),
    path("portfolio/", portfolio, name="portfolio"),
]
