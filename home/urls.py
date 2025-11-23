from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),

    # Search page
    path("search/", views.search_properties, name="search_properties"),

    # Property details
    path("property/<int:id>/", views.property_detail, name="property_detail"),

    #  🌟 REQUIRED AJAX ROUTES FOR YOUR DROPDOWNS
    path("cities/<int:state_id>/", views.get_cities, name="get_cities"),
    path("localities/<int:city_id>/", views.get_localities, name="get_localities"),

    # Debug properties JSON view
    path("debug-properties/", views.debug_properties, name="debug_properties"),
]
