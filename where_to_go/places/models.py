from django.db import models


class Place(models.Model):
    title = models.CharField('название',
                             max_length=200)
    longitude = models.FloatField('долгота')
    langitude = models.FloatField('широта')

    description_short = models.TextField('краткое описание',
                                         blank=True)
    description_long = models.TextField('подробное описание',
                                        blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.ImageField('имя фото места',
                             max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              blank=True,
                              related_name='images_per_place')

    def __str__(self):
        return f'{self.id} {self.name}'
