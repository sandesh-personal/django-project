from django.urls import path
from .views import home_view, root_view_page, portfolio, learning_dtl_view, using_bootstrap_view, temp_inherit_view, about_us_view, contact_us_view

urlpatterns = [
    path("home/", home_view),
    path("", root_view_page,name="root_page"),
    path("portfolio/", portfolio, name="portfolio"),
    path("learning_dtl/", learning_dtl_view, name ="learning_dtl"),
    path("using_bootstrap/", using_bootstrap_view, name ="using_bootstrap"),
    path("temp_inherit/", temp_inherit_view, name ="temp_inherit"),
    path("about_us/", about_us_view, name ="about_us"),
    path("contact_us/", contact_us_view, name ="contact_us"),
]
