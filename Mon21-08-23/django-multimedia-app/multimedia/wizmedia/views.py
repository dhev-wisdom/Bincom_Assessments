import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Audio, Videos
from .upload_form import ImageUploadForm, AudioUploadForm, VideoUploadForm
import os

API_KEY =os.environ.get("API_KEY")

def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    api_key = API_KEY
    api_url = f"https://newsdata.io/api/1/news?apikey={api_key}&q=cryptocurrency "
    response = requests.get(api_url)
    data = response.json()
    news = data.get('results', [])
    return render(request, 'news.html', {'news': news})

def listImages(request):
    images = Image.objects.all()
    upload = upload_image(request)
    return render(request, 'image_list.html', {'images': images, 'upload': upload})

def listAudio(request):
    audio = Audio.objects.all()
    return render(request, 'audio_list.html', {'audio': audio})

def listVideo(request):
    videos = Videos.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_audio(request):
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio')
    else:
        form = AudioUploadForm()
    return render(request, 'upload_audio.html', {'form': form})

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    referrer = request.POST.get('referrer', '/')
    if request.method == 'POST':
        image.delete()
        return redirect(referrer)
    return render(request, 'delete_image.html', {'image': image})

def delete_audio(request, audio_id):
    audio = get_object_or_404(Audio, pk=audio_id)
    referrer = request.POST.get('referrer', '/')
    if request.method == 'POST':
        audio.delete()
        return redirect(referrer)
    return render(request, 'delete_audio.html', {'audio': audio})

def delete_video(request, video_id):
    video = get_object_or_404(Videos, pk=video_id)
    referrer = request.POST.get('referrer', '/')
    if request.method == 'POST':
        video.delete()
        return redirect(referrer)
    return render(request, 'delete_video.html', {'video': video})
