from pathlib import PurePath
from urllib.parse import urlparse

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import (
    Image,
    Place,
)


class Command(BaseCommand):
    help = (
        'Создаёт записи об интересных местах и '
        'их фотографиях в БД.'
    )

    def add_arguments(self, parser):
        help_to_raw_file_url_arg = (
            'URL-адрес json-файла с данными'
        )
        parser.add_argument('raw_file_url',
                            help=help_to_raw_file_url_arg)

    def handle(self, *args, **kwargs):
        raw_file_url = kwargs['raw_file_url']

        response = requests.get(raw_file_url)
        response.raise_for_status()
        place_and_image_raw_data = response.json()
        defaults = {
            "description_short": place_and_image_raw_data['description_short'],
            "description_long": place_and_image_raw_data['description_long'],
            "latitude": place_and_image_raw_data['coordinates']['lat'],
            "longitude": place_and_image_raw_data['coordinates']['lng'],
        }

        place, _ = (Place.objects
                    .get_or_create(title_long=place_and_image_raw_data['title'],
                                   defaults=defaults))

        for image_url in place_and_image_raw_data['imgs']:

            image = Image.objects.create(place=place)

            response = requests.get(image_url)
            response.raise_for_status()

            image_content = ContentFile(response.content)
            disassembled_url = urlparse(image_url)
            image_name = PurePath(disassembled_url.path).name
            image.name.save(image_name, image_content, save=True)

        success_added_place_and_image_msg = (
            'Интересное место и фото добавлены в БД '
            f'из источника: {raw_file_url}'
        )
        self.stdout.write(self.style.SUCCESS(success_added_place_and_image_msg))
