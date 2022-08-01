from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from article.models import Articles
from django.utils import timezone
from django.shortcuts import render, redirect

def index(request):
    count = Articles.objects.count()
    q = Articles(url='http://testurl.com', title='test_title', content='tests_content', date=timezone.now())
    q.save()
    return HttpResponse("테스트 중입니다." + str(count))

def post(request):
    return render(request, 'article/post.html')

def post_result(request):
    if request.POST.get('title') != None and request.POST.get('content') != None:
        q = Articles(url='http://testurl.com', title=request.POST.get('title'), content=request.POST.get('content'), date=timezone.now())
        q.save()

    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, 'article/post_result.html', context)