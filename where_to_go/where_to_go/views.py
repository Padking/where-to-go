from django.shortcuts import render
from django.urls import reverse

from geojson import (
    Feature,
    FeatureCollection,
    Point,
)

from places.models import (
    Place,
)


def show_map(request):
    places = Place.objects.all()
    features = []
    for place in places:
        point = (place.longitude, place.latitude)
        properties = {
            'title': place.title_short,
            'placeId': place.place_identifier,
            'detailsUrl': reverse('places:place',
                                  kwargs={'place_id': place.id}),
        }
        feature = Feature(geometry=Point(point),
                          properties=properties)
        features.append(feature)

    feature_collection = FeatureCollection(features)

    context = {
        'places': feature_collection,
    }

    return render(request, 'index.html',
                  context=context)
