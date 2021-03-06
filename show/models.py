from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.utils import timezone
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


def get_or_create_parts():
    parts = Parts.objects.get_or_create()
    return parts


class Parts(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    cloth_name = models.CharField(verbose_name='Brand Name', max_length=50)
    date_purchase = models.DateField(verbose_name='購入日', null=True, blank=True)
    season = models.CharField(verbose_name='季節', max_length=5, choices=SEASONS_CHOICES)
    part = models.ForeignKey(Parts, verbose_name="部位",
                             on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='写真', upload_to='photos/', null=True, blank=True,
                              height_field=None, width_field=None, max_length=None)
    price = models.IntegerField(verbose_name='価格', validators=[
                                validators.MinValueValidator(0)], null=True, blank=True)
    favorite = models.BooleanField(("お気に入り"), null=True, blank=True, default=False)

    # user = models.ForeignKey(CustomUser, verbose_name='ユーザ', on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth_name
