from django.db import models


class Urls(models.Model):
    url_code = models.SlugField(max_length=6, primary_key=True)
    full_url = models.URLField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'URL: {self.full_url}, code: {self.url_code}, created: {self.creation_date}'
