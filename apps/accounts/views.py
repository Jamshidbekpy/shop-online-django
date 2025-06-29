from django.shortcuts import render
from django.views import View


# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

# class LogoutView(View):
#     def get(self, request):
#         return render(request, 'logout.html')
    
