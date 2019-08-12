from django.shortcuts import render
from django.http import HttpResponse 
from .models import ExImp
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer


# Create your views here.
def index(request):
    #return  HttpResponse('Hello from eximp')

    eximp = ExImp.objects.all()[:10]

    context = {
        'title': 'Latest ExImp',
        'eximp': eximp
    }

    return render(request, 'eximp/index.html', context)

def details(request, id):
        exim = ExImp.objects.get(id=id)

        context = {
            'exim': exim
        }
        return render(request, 'eximp/details.html', context)

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
