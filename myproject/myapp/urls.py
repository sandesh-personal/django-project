from django.urls import path
from .views import home_view, root_view_page, portfolio, learning_dtl_view, using_bootstrap_view

urlpatterns = [
    path("home/", home_view),
    path("", root_view_page,name="rootpage"),
    path("portfolio/", portfolio, name="portfolio"),
    path("learning_dtl/", learning_dtl_view, name ="learning_dtl"),
    path("using_bootstrap/", using_bootstrap_view, name ="using_bootstrap"),
]
