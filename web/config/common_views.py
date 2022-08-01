from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from article.models import Articles

def index(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, 'common/main.html', context)

def login(request):
    return render(request, 'common/login.html')