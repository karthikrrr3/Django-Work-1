from django.shortcuts import render

# Create your views here.



#Function Based


from django.http import HttpResponse
# def home(request):
#     if (request.method=='GET'):
#         return HttpResponse('Welcome to Django.')


def indexview(request):
    if (request.method == 'GET'):
        return  HttpResponse('Index Page')



    #Class Based

from django.views import View
from django.http import HttpResponse
class home(View):
    def get(self, request):
        return HttpResponse('Welcome to Django.')