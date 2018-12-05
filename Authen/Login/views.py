from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Create your views here.

class ClassIndex(View):
    def get(self, request):
        return HttpResponse("Xin chao")


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        user_name = request.POST.get('tendangnhap')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse("user k ton tai")
        login(request, my_user)
        return render(request, 'Login/success.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/login'

    def get(self, request):
        return HttpResponse("day la view user")


@decorators.login_required(login_url='/login/login')
def view_product(request):
    return HttpResponse("Xem san pham ")


class AddPost(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'Login/add_post.html', {'fm': a})

    def post(self, request):
        a = PostForm(request.POST)
        if not a.is_valid():
            return HttpResponse("nhap sai du lieu r")
        # cache reload tu database user
        print(request.user.get_all_permissions)
        if request.user.has_perm('Login.add_post'):
            a.save()
        else:
            return HttpResponse("may k có quyèn")
        return HttpResponse("oke")
