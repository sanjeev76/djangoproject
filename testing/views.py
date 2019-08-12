from django.shortcuts import render, get_object_or_404
#django.contrib.auth.decorators import login_required
from .models import Testing


#@login_required
# Create your views here.
def testing_detail(request, pk):
    testing = get_object_or_404(Testing, pk=pk)
    return render(request, 'testing_detail.html', {'testing': testing})
