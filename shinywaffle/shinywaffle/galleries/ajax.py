
from .models import Gallery, Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

"""
We know that @csrf_exempt is a really bad practice but we need
it if we want this to work in production in HTTPS
"""
@csrf_exempt
def delete_gallery(request):
    id = request.POST.get('id')
    Gallery.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Gallery deleted correctly'}
    return JsonResponse(data, status=200)


@csrf_exempt
def delete_image(request):
    id = request.POST.get('id')
    Image.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Image deleted correctly'}
    return JsonResponse(data, status=200)
