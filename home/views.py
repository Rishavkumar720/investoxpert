from django.shortcuts import render,get_object_or_404
from .models import State, City, Locality, Property

from django.http import JsonResponse

def home_view(request):
    states = State.objects.all()
    return render(request, "home.html", {"states": states})



def get_cities(request, state_id):
    cities = City.objects.filter(state_id=state_id)
    data = [{"id": c.id, "name": c.name} for c in cities]
    return JsonResponse({"cities": data})


def get_localities(request, city_id):
    localities = Locality.objects.filter(city_id=city_id)
    data = [{"id": l.id, "name": l.name} for l in localities]
    return JsonResponse({"localities": data})

def search_properties(request):
    import logging
    logger = logging.getLogger(__name__)
    state_id = request.GET.get("state")
    city_id = request.GET.get("city")
    locality_id = request.GET.get("locality")
    bhk = request.GET.get("bhk")

    logger.info(f"Search filters - state: {state_id}, city: {city_id}, locality: {locality_id}, bhk: {bhk}")

    properties = Property.objects.all()

    if locality_id:
        properties = properties.filter(locality_id=locality_id)
        if city_id:
            properties = properties.filter(locality__city_id=city_id)
        if state_id:
            properties = properties.filter(locality__city__state_id=state_id)
    elif city_id:
        properties = properties.filter(city_id=city_id)
        if state_id:
            properties = properties.filter(city__state_id=state_id)
    elif state_id:
        properties = properties.filter(state_id=state_id)

    if bhk:
        properties = properties.filter(bhk__icontains=bhk.strip())

    count = properties.count()
    logger.info(f"Properties found count: {count}")

    # Pass debugging info to the template
    debug_info = {
        "state_id": state_id,
        "city_id": city_id,
        "locality_id": locality_id,
        "bhk": bhk,
        "matched_count": count,
    }

    return render(request, "property_list.html", {"properties": properties, "debug_info": debug_info})


def property_detail(request, id):
    property_obj = get_object_or_404(Property, id=id)
    # Preprocess amenities as list
    amenities_list = []
    if property_obj.amenities:
        amenities_list = [item.strip() for item in property_obj.amenities.split(",")]
    # Use effective map embed URL property for valid embed link
    effective_map_url = property_obj.effective_map_embed_url
    return render(request, "property_detail.html", {"p": property_obj, "amenities_list": amenities_list, "effective_map_url": effective_map_url})

def debug_properties(request):
    # Simple JSON response showing all properties and their main filter fields
    from django.http import JsonResponse
    props = Property.objects.all().values("id", "title", "state_id", "city_id", "locality_id", "bhk")
    return JsonResponse(list(props), safe=False)

def distinct_bhk_values(request):
    from django.http import JsonResponse
    bhk_values = Property.objects.values_list('bhk', flat=True).distinct()
    bhk_values_list = list(bhk_values)
    return JsonResponse({"distinct_bhk_values": bhk_values_list})
