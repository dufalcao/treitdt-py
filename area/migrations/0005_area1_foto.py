# Generated by Django 3.2.2 on 2021-05-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0004_alter_area1_geom'),
    ]

    operations = [
        migrations.AddField(
            model_name='area1',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
