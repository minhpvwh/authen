from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin


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
