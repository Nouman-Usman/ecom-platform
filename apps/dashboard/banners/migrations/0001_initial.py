# Generated by Django 2.2.5 on 2020-07-03 15:14

import apps.dashboard.banners.models
from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Banner Title')),
                ('slug', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='title', unique=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.dashboard.banners.models.get_tenant_specific_upload_folder, verbose_name='Banner Image')),
                ('content', models.TextField(verbose_name='Content')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='banners.Banner')),
            ],
        ),
    ]
