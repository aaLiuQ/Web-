from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    print(request.META['CONTENT_TYPE'])
    # return HttpResponse("hello word")
    context = {'city': 'beijing'}
    return render(request, 'index.html', context)
