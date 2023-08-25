from django.db import models

class Image(models.Model):
    """
    Image Model
    """
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    image_description = models.TextField()

class Videos(models.Model):
    """
    Video Model
    """
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    video_description = models.TextField()

class Audio(models.Model):
    """
    Audio Model
    """
    audio = models.FileField(upload_to='audio/')
    title = models.CharField(max_length=255)
    audio_description = models.TextField()