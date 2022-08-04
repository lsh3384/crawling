from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from article.models import Articles
from django.utils import timezone
from django.shortcuts import render, redirect

from forms import UploadFileForm
from ..models import UploadFileModel

from django.core.paginator import Paginator

def index(request):
    count = Articles.objects.count()
    q = Articles(url='http://testurl.com', title='test_title', content='tests_content', date=timezone.now())
    q.save()
    return HttpResponse("테스트 중입니다." + str(count))

def post(request):
    if request.method == 'POST':
        if request.POST.get('title') != None and request.POST.get('content') != None:
            q = Articles(url='http://testurl.com', title=request.POST.get('title'), content=request.POST.get('content'),
                         date=timezone.now())
            q.save()
            page = request.GET.get('page', '1')  # 페이지
            articles = Articles.objects.order_by('-date')
            paginator = Paginator(articles, 10)  # 페이지당 10개씩 보여주기
            page_obj = paginator.get_page(page)
            context = {'articles': page_obj}
            return render(request, 'article/post_result.html', context)

    else:
        return render(request, 'article/post.html')


def post_result(request):
    page = request.GET.get('page')  # 페이지
    articles = Articles.objects.order_by('-date')
    paginator = Paginator(articles, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'articles': page_obj}
    return render(request, 'article/post_result.html', context)

def post_detail(request):
    post = request.GET.get('post_id')  # 페이지
    article = Articles.objects.get(id=post)
    context = {'article': article}
    return render(request, 'article/post_detail.html', context)


def upload_image_form(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = UploadFileForm()
    context = { 'form': form }
    return render(request, 'article/form_test.html', context)