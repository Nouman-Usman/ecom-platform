# Generated by Django 2.2.5 on 2019-12-08 15:02

from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.slugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerConfigurableMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='categories', verbose_name='Image')),
                ('slug', oscar.models.fields.slugfield.SlugField(max_length=255, verbose_name='Slug')),
                ('category', models.ManyToManyField(blank=True, related_name='partner_menu_items', to='catalogue.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Configurable MenuItem',
                'verbose_name_plural': 'Configurable MenuItems',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerConfigurableMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('is_primary', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='sites.Site')),
            ],
        ),
    ]