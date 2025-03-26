from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageUploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils import timezone
import os

@login_required
def images_list(request):
    images = Image.objects.all()
    return render(request,  'images/images_list.html', {'images': images})

@login_required
def image_page(request, slug):
    image = Image.objects.get(slug=slug)
    return render(request,  'images/image_page.html', {'image': image})

@login_required
def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.slug = slugify(f'{timezone.now()}_{image.author.username}_{image.title}')
            image.save()
            return redirect('images:list')
    else:
        form = ImageUploadForm()
    return render(request, 'images/image_upload.html', {'form': form})

@login_required
def delete_image(request, slug):
    image = get_object_or_404(Image, slug=slug)

    if request.method == 'POST':
        if image.banner:
            if os.path.isfile(image.banner.path):
                os.remove(image.banner.path)
        image.delete()
        messages.success(request, "Image deleted successfully.")
        return redirect('images:list')

    messages.error(request, "Invalid request method.")
    return redirect('images:page', slug=slug)