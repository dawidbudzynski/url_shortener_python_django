# Generated by Django 2.2 on 2019-04-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('url_code', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('full_url', models.URLField(max_length=500)),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
