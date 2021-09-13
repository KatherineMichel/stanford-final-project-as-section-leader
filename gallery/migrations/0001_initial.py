# Generated by Django 3.2.7 on 2021-09-13 02:15

from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.upload_gallery_image)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.artwork')),
            ],
        ),
    ]
