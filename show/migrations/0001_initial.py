# Generated by Django 3.1.5 on 2021-01-29 05:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('アウター', 'アウター'), ('トップス', 'トップス'), ('ボトムス', 'ボトムス'), ('靴', '靴'), ('ストール', 'ストール')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_name', models.CharField(max_length=50)),
                ('date_purchase', models.DateField(blank=True, null=True)),
                ('season', models.CharField(choices=[('春', '春'), ('夏', '夏'), ('秋', '秋'), ('冬', '冬')], max_length=5)),
                ('image', models.ImageField(upload_to='photos/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'HEIF'])])),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.parts', verbose_name='parts')),
            ],
        ),
    ]