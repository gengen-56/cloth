from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
# Create your models here.

SEASONS_CHOICES = (
    ('春', '春'),
    ('夏', '夏'),
    ('秋', '秋'),
    ('冬', '冬'),
)

PART_CHOICES = (
    ('アウター', 'アウター'),
    ('トップス', 'トップス'),
    ('ボトムス', 'ボトムス'),
    ('靴', '靴'),
    ('ストール', 'ストール'),

)


class Parts(models.Model):
    name = models.CharField(max_length=50, choices=PART_CHOICES)

    def __str__(self):
        return self.name


class Post(models.Model):
    cloth_name = models.CharField(max_length=50)
    date_purchase = models.DateField(null=True, blank=True)
    season = models.CharField(max_length=5, choices=SEASONS_CHOICES)
    part = models.ForeignKey(Parts, verbose_name="parts", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/',
                              validators=[FileExtensionValidator(['jpg', 'png', 'HEIC'])],
                              height_field=None, width_field=None, max_length=None)
    """image = ImageSpecField(source="photos", processors=[ResizeToFill(500, 300)],
                           validators=[FileExtensionValidator(['jpg', 'png', 'HEIC'])],
                           format='JPEG', options={'quality': 60})
    """

    def __str__(self):
        return self.cloth_name
