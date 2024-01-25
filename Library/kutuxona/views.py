from django.shortcuts import render, redirect

from .models import *


def hamma_kitoblar(reqest):
    natija=Kitob.objects.all()
    kiritilgan_kitob=reqest.GET.get("nomi")
    if kiritilgan_kitob is not None:
        natija=Kitob.objects.filter(nom__contains=kiritilgan_kitob)
    date={
            "books":natija

    }
    return render(reqest,'kitoblar.html',date)
def Student(reqest):
    natija=Talaba.objects.all()
    kiritilgan_ism=reqest.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija=Talaba.objects.filter(ism__contains=kiritilgan_ism)

    talaba={
            "students":natija
    }
    return render(reqest, 'Student.html', talaba)

def Bitiruvchi(reqest):
    talaba={
            "students":Talaba.objects.filter(kurs=4)
    }
    return render(reqest, 'Bitiruvchi.html', talaba)

def oqigan(reqest):
    talaba={
            "students":Talaba.objects.filter(kitoblar_soni__gt=0)
    }
    return render(reqest, 'Bitiruvchi.html', talaba)

def A_lar(reqest):
    talaba={
            "students":Talaba.objects.filter(ism__contains='a')
    }
    return render(reqest, 'Bitiruvchi.html', talaba)

def bitta_talaba(reqest,pk):
    talaba={
            "talaba":Talaba.objects.get(id=pk)
    }
    return render(reqest, 'bitta_talaba.html', talaba)

def erkak_muallif(reqest):
    mualliflar={
            "muallif":Muallif.objects.filter(jins="Erkak")
    }
    return render(reqest, 'erkak_muallif.html', mualliflar)

def talaba_ochir(reqest,pk):

        Talaba.objects.get(id=pk).delete()
        return redirect("/student/")


def kitob_ochir(reqest, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/books/")

def hamma_mualliflar(reqest):

    date={
            "mualliflar":Muallif.objects.all()

    }
    return render(reqest, 'Muallif.html', date)


def bitta_muallif(reqest,pk):
    date={
            "muallif":Muallif.objects.get(id=pk)
    }
    return render(reqest, 'bitta_muallif.html', date)


def sahifa_kitoblar(reqest):

    date={
            "kitoblar":Kitob.objects.all().order_by("-olingan_sana")[0,3]

    }
    return render(reqest, 'records.html', date)
def kitob_tirik_muallif(reqest):
    date={
        "kitoblar":Kitob.objects.filter(muallif="Muallif__tirik=True`")
    }
    return render(reqest, 'TirikMuallifKitoblari.html', date)

def badiy_kitob(reqest):
    date={
        "kitoblar":Kitob.objects.filter(janr="badiy")
    }
    return render(reqest, 'TirikMuallifKitoblari.html', date)



