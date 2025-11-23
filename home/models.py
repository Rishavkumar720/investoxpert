from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.state.name})"


class Locality(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="localities")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.city.name}"


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # filter fields
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)

    bhk = models.CharField(max_length=10)  # "1 BHK", "2 BHK"

    price_min = models.CharField(max_length=50)
    price_max = models.CharField(max_length=50)

    image = models.URLField(blank=True)  # optional

    about = models.TextField(blank=True)
    configuration = models.CharField(max_length=100, blank=True)
    amenities = models.CharField(max_length=255, blank=True)
    developer = models.CharField(max_length=255, blank=True)
    map_embed_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    @property
    def effective_map_embed_url(self):
        # Return valid embed URL, fallback to constructed address map URL if blank or invalid
        if self.map_embed_url and self.map_embed_url.strip():
            # return saved URL
            return self.map_embed_url.strip()
        # else compose address-based URL
        address = f"{self.locality.name}, {self.city.name}, {self.state.name}"
        from urllib.parse import quote_plus
        encoded_address = quote_plus(address)
        # public embed without API key
        return f"https://maps.google.com/maps?q={encoded_address}&output=embed"
