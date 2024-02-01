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
    path('talaba_ochir/<int:pk>/', talaba_ochir),
    path('talabalar/<int:pk>/tahrirlash/', talaba_tahrirlash),
    path('muallif/<int:pk>/tahrirlash/', muallif_tahrirlash),
    path('muallif_ochir/<int:pk>/', muallif_ochir),
    path('kitob_ochir/<int:pk>/', kitob_ochir),
    path('bitta_record/<int:pk>/', bitta_record),
    path('hamma_mualliflar/', hamma_mualliflar),
    path('bitta_muallif/<int:pk>/', bitta_muallif),
    path('sahifa_kitob/', sahifa_kitoblar),
    path('kitob_tirik_muallif/', kitob_tirik_muallif),
    path('kitob_son_muallif/', kitob_tirik_muallif),
    path('badiy_kitob/', badiy_kitob),
    path('katta_muallif/', katta_muallif),
    path('bitiruvchi/', bitiruvchi),
    path('records/', records),
    path('records/<int:pk>/tahrirlash/', record_tahrirlash),
    path('record_ochir/<int:pk>/', record_ochir),
    path('kutubxonachilar/', kutubxonachilar),
    path('kutubxonachilar/<int:pk>/tahrirlash/', kutubxonachi_tahrirlash),
]
