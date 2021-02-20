from django.shortcuts import render
from .models import Variables

def page(request):
    variables = Variables.objects.all()
    return render(request, 'table.html', {'variables': variables})
