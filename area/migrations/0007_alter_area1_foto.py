# Generated by Django 3.2.2 on 2021-05-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0006_alter_area1_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area1',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
