from django.db import models


class Image(models.Model):
    username = models.CharField(max_length=255)
    file = models.ImageField(upload_to='media/images')

    def get_username(self):
        return self.username
