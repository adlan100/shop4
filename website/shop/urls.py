from django.urls import path
from .views import main_home, main_kup
from .views import main_shop
from .views import main_kup
from .views import main_kom
from .views import main_spo
from .views import main_tv

urlpatterns = [
    path('main',main_home,name='main'),
    path('mag',main_shop,name='shop'),
    path('kup',main_kup,name='kup'),
    path('kom',main_kom,name='kom'),
    path('spo',main_spo,name='spo'),
    path('tv', main_tv, name='tv'),
]