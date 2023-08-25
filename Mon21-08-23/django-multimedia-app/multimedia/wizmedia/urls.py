from django.urls import path
from .views import home, listImages, listAudio, listVideo, upload_image, upload_audio, upload_video, about, news
from .views import delete_image, delete_audio, delete_video

urlpatterns = [
    path('', home, name='home'),
    path('images/', listImages, name='images'),
    path('audio/', listAudio, name='audio'),
    path('video/', listVideo, name='videos'),
    path('upload/image/', upload_image, name='upload-image'),
    path('upload/audio/', upload_audio, name='upload-audio'),
    path('upload/video/', upload_video, name='upload-video'),
    path('delete/image/<int:image_id>', delete_image, name='delete_image'),
    path('delete/audio/<int:audio_id>', delete_audio, name='delete_audio'),
    path('delete/video/<int:video_id>', delete_video, name='delete_video'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
]