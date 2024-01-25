
from django.contrib import admin
from django.urls import path
from kutuxona.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', hamma_kitoblar),
    path('student/', Student),
    path('bitiruvchi/', Bitiruvchi),
    path('oqigan/', oqigan),
    path('alar/', A_lar),
    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('erkak_muallif/', erkak_muallif),
    path('talaba_ochir/', talaba_ochir),
    path('kitob_ochir/<int:pk>/', kitob_ochir),
    path('hamma_mualliflar/', hamma_mualliflar),
    path('bitta_muallif/<int:pk>/', bitta_muallif),
    path('sahifa_kitob/', sahifa_kitoblar),
    path('kitob_tirik_muallif/', kitob_tirik_muallif),
    path('badiy_kitob/', badiy_kitob),
]
