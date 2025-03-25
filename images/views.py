from django.shortcuts import render
from .models import Image

# Create your views here.
def images_list(request):
    images = Image.objects.all()
    return render(request,  'images/images_list.html', {'images': images})

def image_page(request, slug):
    image = Image.objects.get(slug=slug)
    return render(request,  'images/image_page.html', {'image': image})
