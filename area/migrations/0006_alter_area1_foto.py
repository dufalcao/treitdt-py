# Generated by Django 3.2.2 on 2021-05-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0005_area1_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area1',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='area'),
        ),
    ]
