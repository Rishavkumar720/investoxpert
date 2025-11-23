from django.contrib import admin
from .models import State, City, Locality, Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "state", "city", "locality", "bhk", "price_min", "price_max")
    search_fields = ("title", "bhk", "state__name", "city__name", "locality__name")
    list_filter = ("state", "city", "bhk")

    # Show ALL fields in admin form
    fields = (
        "title",
        "description",
        "state",
        "city",
        "locality",
        "bhk",
        "price_min",
        "price_max",
        "image",
        "about",
        "configuration",
        "amenities",
        "developer",
        "map_embed_url",
    )

admin.site.register(State)
admin.site.register(City)
admin.site.register(Locality)
