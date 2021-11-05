from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import (
    Place,
)


def map_points(request, place_id):

    place = get_object_or_404(Place, pk=place_id)
    response_data = {
        'title': place.title_long,
        'imgs': [image.name.url for image in place.images_per_place.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(response_data, safe=False,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 4,
                        })
