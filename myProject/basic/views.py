from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample(request):
    return HttpResponse('hello world')
def sample1(request):
    return HttpResponse('hello django')
def sample2(request):
    data={'name':'john','age':22,'city':'newyork'}
    return JsonResponse(data)
def sample3(request):
    # data={'python','django','java','html','css'}
    data={'result':['python','django','java','html','css']}
    return JsonResponse(data,safe=False)
def dynamicResponse(reuest):
    name=reuest.GET.get('name','')
    # return HttpResponse(f'hello {name}')
    # age=reuest.GET.get('age')
    city=reuest.GET.get('city','hyd')
    return HttpResponse(f'hello {name} from {city}')
    # response=f'hello {name}, your age is {age} and you live in {city}'
    # return HttpResponse(response)
