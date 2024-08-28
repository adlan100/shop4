from django.shortcuts import render
from django.http import HttpResponse

def main_home(request):
    return render(request,'shop/home.html')

def main_shop(request):
    return render(request,'mag/shop.html')

def main_kup(request):
    return render(request,'kup/kup.html')

def main_kom(request):
    return render(request,'kom/kom.html')

def main_spo(request):
    return render(request,'spo/spo.html')

def main_tv(request):
    return render(request,'tv/tv.html')