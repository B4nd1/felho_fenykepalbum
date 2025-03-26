from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

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
            image.slug = slugify(image.title)
            image.save()
            return redirect('images:list')
    else:
        form = ImageUploadForm()
    return render(request, 'images/image_upload.html', {'form': form})