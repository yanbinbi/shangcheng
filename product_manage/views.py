from django.shortcuts import render

# Create your views here.
#首页
def home(request):
    return render(request, "product_manage/home.html", locals())

# 个人中心
def index(request):
    return render(request, "product_manage/index.html", locals())