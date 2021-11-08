from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Place(models.Model):
    title_long = models.CharField('подробное название',
                                  max_length=200)
    title_short = models.CharField('краткое название',
                                   max_length=200)
    place_identifier = models.CharField('идентификатор',
                                        max_length=200)
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    description_short = models.TextField('краткое описание',
                                         blank=True)
    description_long = models.TextField('подробное описание',
                                        blank=True)

    def __str__(self):
        return self.title_long


class Image(models.Model):
    name = models.ImageField('имя фото места',
                             max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              blank=True,
                              related_name='images_per_place')
    position = models.PositiveIntegerField('позиция',
                                           default=0)

    @property
    def get_preview(self):
        html_code = (
            '<img src="{url}" style="max-height:{max_height}px">'
        )
        if self.name:
            return format_html(mark_safe(html_code),
                               url=self.name.url,
                               max_height=200)

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.id} {self.place.title_long}'
