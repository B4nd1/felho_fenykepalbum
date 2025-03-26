from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def images_list(request):
    images = Image.objects.all()
    return render(request,  'images/images_list.html', {'images': images})

@login_required
def image_page(request, slug):
    image = Image.objects.get(slug=slug)
    return render(request,  'images/image_page.html', {'image': image})
