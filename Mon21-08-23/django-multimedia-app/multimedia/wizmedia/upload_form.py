from django import forms
from .models import Image, Videos, Audio

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'image_description']

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'video', 'video_description']

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio', 'audio_description']
