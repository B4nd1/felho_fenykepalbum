from django.shortcuts import render

# Create your views here.
def images_list(request):
    return render(request,  'images/images_list.html')