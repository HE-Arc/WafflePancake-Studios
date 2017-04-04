
from .models import Gallery, Image
from django.http import JsonResponse


def delete_gallery(request):
    id = request.POST.get('id')
    Gallery.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Gallery deleted correctly'}
    return JsonResponse(data, status=200)


def delete_image(request):
    id = request.POST.get('id')
    Image.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Image deleted correctly'}
    return JsonResponse(data, status=200)
