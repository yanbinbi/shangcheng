from django.shortcuts import render
import logging
from user_manage.forms import EmailRegisterForm, PhoneRegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from user_manage.models import User

# Create your views here.
logger = logging.getLogger("user_manage.views")

#首页
def home(request):
    return render(request, "user_manage/home.html", locals())

# 个人中心
def index(request):
    return render(request, "user_manage/index.html", locals())

# 跳转用户注册页面
def register(request):
    email_register_form = EmailRegisterForm()
    phone_register_form = PhoneRegisterForm()
    return render(request, "user_manage/register.html", locals())

# 邮箱注册
def email_register(request):
    try:
        if request.method == "POST":
            email_register_form = EmailRegisterForm(request.POST)
            if email_register_form.is_valid():
                user = User.objects.create(email=email_register_form.cleaned_data["email"],
                                           password=make_password(email_register_form.cleaned_data["password"], 'ybb', 'pbkdf2_sha256'))
                user.save()
                return render(request, "product_manage/index.html", locals())
            else:
                return render(request, "user_manage/failure.html", {"reason": email_register_form.errors})
        else:
            email_register_form = EmailRegisterForm()

    except Exception as e:
        logger.error(e)
        print(e)

    return render(request, 'user_manage/register.html', locals())

# 手机注册
def phone_register(request):
    try:
        if request.method == "POST":
            phone_register_form = PhoneRegisterForm(request.POST)
            if phone_register_form.is_valid():
                user = User.objects.create(phone_num=phone_register_form.cleaned_data['phone_num'],
                                           password=phone_register_form.cleaned_data['password'])
                user.save()
            else:
                return render(request, "user_manage/failure.html", {"reason": phone_register_form.errors})
        else:
            phone_register_form = PhoneRegisterForm()
    except Exception as e:
        logger.error(e)

    return render(request, 'user_manage/register.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 将用户的注册邮箱或手机默认设置为username
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]

                # 判断获得的username是邮箱还是手机号码
                user = User.objects.filter(email__exact=username, password__exact=make_password(password, 'ybb', 'pbkdf2_sha256'))
                if user is None:
                    user = User.objects.filter(phone__exact=username, password__exact=make_password(password, 'ybb', 'pbkdf2_sha256'))
                # 如果用户存在
                if user is not None:
                    # 登录成功，页面跳转到个人中心
                    return render(request, "user_manage/index.html", locals())
                else:
                    return render(request, 'user_manage/failure.html', {'reason': '登录验证失败'})
            else:
                return render(request, "user_manage/failure.html", {"reason": login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
        print(e)
    return render(request, "user_manage/login.html", locals())
