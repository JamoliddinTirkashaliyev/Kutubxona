from django.shortcuts import render, redirect
from .models import *
from .forms import *


def hamma_kitoblar(reqest):
    if reqest.method == "POST":
        Kitob.objects.create(
            nom=reqest.POST.get("nom"),
            muallif=Muallif.objects.get(id=reqest.POST.get("m")),
            sahifa=reqest.POST.get("s"),
            janr=reqest.POST.get("j"),
        )
        return redirect("/books/")
    natija = Kitob.objects.all()
    kiritilgan_kitob = reqest.GET.get("nomi")
    if kiritilgan_kitob is not None:
        natija = Kitob.objects.filter(nom__contains=kiritilgan_kitob)
    date = {
        "books": natija,
        "mualliflar": Muallif.objects.all(),

    }
    return render(reqest, 'kitoblar.html', date)


def Student(reqest):
    if reqest.method == "POST":

        date = TalabaForm(reqest.POST)
        if date.is_valid():
            Talaba.objects.create(
                ism = date.cleaned_data['ism'],
                kitoblar_soni = date.cleaned_data['kitoblar_soni'],
                kurs = date.cleaned_data['kurs'],
            )
        # Talaba.objects.create(
        #     ism=reqest.POST.get("ismi"),
        #     kurs=reqest.POST.get("k"),
        #     kitoblar_soni=reqest.POST.get("k_s")
        # )
        return redirect("/student/")

    natija = Talaba.objects.all()
    kiritilgan_ism = reqest.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)

    talaba = {
        "students": natija,
        'form': TalabaForm()
    }
    return render(reqest, 'Student.html', talaba)


def Bitiruvchi(reqest):
    talaba = {
        "students": Talaba.objects.filter(kurs=4)
    }
    return render(reqest, 'Bitiruvchi.html', talaba)


def oqigan(reqest):
    talaba = {
        "students": Talaba.objects.filter(kitoblar_soni__gt=0)
    }
    return render(reqest, 'Bitiruvchi.html', talaba)


def A_lar(reqest):
    talaba = {
        "students": Talaba.objects.filter(ism__contains='a')
    }
    return render(reqest, 'Bitiruvchi.html', talaba)


def bitta_talaba(reqest, pk):
    talaba = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(reqest, 'bitta_talaba.html', talaba)


def erkak_muallif(reqest):
    mualliflar = {
        "muallif": Muallif.objects.filter(jins="Erkak")
    }
    return render(reqest, 'erkak_muallif.html', mualliflar)


def talaba_ochir(reqest, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/student/")


def kitob_ochir(reqest, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/books/")


def hamma_mualliflar(reqest):
    if reqest.method == "POST":
        data = MuallifForm(reqest.POST)
        if data.is_valid():
            Muallif.objects.create(
                ism=data.cleaned_data['ism'],
                jins=data.cleaned_data['jins'],
                tugulgan_sana=data.cleaned_data['tugulgan_sana'],
                tirik=data.cleaned_data['tirik'],
                kitoblar_soni=data.cleaned_data['kitoblar_soni'],
            )
        # Muallif.objects.create(
        #     ism=reqest.POST.get("ismi"),
        #     jins=reqest.POST.get("jins"),
        #     tugilgan_sana=reqest.POST.get("t_s"),
        #     tirik=reqest.POST.get("t") == "on",
        #     kitoblar_soni=reqest.POST.get("k_s"),
        #
        # )
        return redirect("/hamma_mualliflar/")
    natija = Muallif.objects.all()
    kiritilgan_ism = reqest.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Muallif.objects.filter(ism__contains=kiritilgan_ism)
    date = {
        "mualliflar": natija,
        'forms': MuallifForm(),

    }
    return render(reqest, 'Muallif.html', date)


def bitta_muallif(reqest, pk):
    date = {
        "muallif": Muallif.objects.get(id=pk)
    }
    return render(reqest, 'bitta_muallif.html', date)


def sahifa_kitoblar(reqest):
    date = {
        "kitoblar": Kitob.objects.all().order_by("-sahifa")[0:3]

    }
    return render(reqest, 'Kitoblar.html', date)


def kitob_tirik_muallif(reqest):
    date = {
        "kitoblar": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(reqest, 'TirikMuallifKitoblari.html', date)


def badiy_kitob(reqest):
    date = {
        "kitoblar": Kitob.objects.filter(janr="badiy")
    }
    return render(reqest, 'TirikMuallifKitoblari.html', date)


def katta_muallif(reqest):
    date = {
        "mualliflar": Muallif.objects.all().order_by("-tugilgan_sana")[0:3]

    }
    return render(reqest, 'Muallif.html', date)


def kitob_son_muallif(reqest):
    date = {
        "kitoblar": Kitob.objects.filter(muallif__kitoblar_soni__lt=10)
    }
    return render(reqest, 'TirikMuallifKitoblari.html', date)


def bitta_record(reqest, pk):
    date = {
        "record": Record.objects.get(id=pk)
    }
    return render(reqest, 'bitta_kitob.html', date)


def bitiruvchi(reqest):
    date = {
        "students": Record.objects.filter(talaba__kurs=4)
    }
    return render(reqest, 'records.html', date)


def records(reqest):
    if reqest.method == "POST":
        data = RecordForm(reqest.POST)
        if data.is_valid():
            data.save()
        return redirect("/records/")
    natija = Record.objects.all()
    kiritilgan_ism = reqest.GET.get("nomi")
    if kiritilgan_ism is not None:
        natija = Record.objects.filter(talaba__contains=kiritilgan_ism)
    date = {
        "recordlar" : natija,
        'form': RecordForm(),
    }
    return render(reqest, 'records.html', date)


def muallif_ochir(reqest, pk):
    Muallif.objects.get(id=pk).delete()
    return redirect("/hamma_mualliflar/")


def record_ochir(reqest, pk):
    Record.objects.get(id=pk).delete()
    return redirect("/records/")


def talaba_tahrirlash(reqest, pk):
    if reqest.method == "POST":
        talaba = Talaba.objects.get(id=pk)
        talaba.ism = reqest.POST['ismi']
        talaba.kitoblar_soni = reqest.POST['k_s']
        talaba.kurs = reqest.POST['k']
        talaba.save()
        return redirect('/student/')
    context = {
        'talaba': Talaba.objects.get(id=pk)
    }
    return render(reqest, 'talaba_tahrirlash.html', context)


def muallif_tahrirlash(reqest, pk):
    if reqest.method == "POST":
        muallif = Muallif.objects.get(id=pk)
        muallif.ism = reqest.POST['ismi']
        muallif.jins = reqest.POST['jins']
        muallif.tugilgan_sana = reqest.POST['t_s']
        muallif.tirik = reqest.POST.get('tirik') == 'on'
        muallif.kitoblar_soni = reqest.POST['k_s']
        muallif.save()
        return redirect('/hamma_mualliflar/')
    context = {
        'muallif': Muallif.objects.get(id=pk)
    }
    return render(reqest, 'muallif_tahrirlash.html', context)

def kutubxonachilar(reqest):
    if reqest.method == "POST":
        data = KutubxonachiForm(reqest.POST)
        if data.is_valid():
            data.save()
        return redirect("/kutubxonachilar/")

    context = {
        'kutubxonachilar': Kutubxonachi.objects.all(),
        'form': KutubxonachiForm(),
    }
    return render(reqest, 'kutubxonachilar.html', context)
def kutubxonachi_tahrirlash(reqest, pk):
    if reqest.method == "POST":
        kutubxonachi = Kutubxonachi.objects.get(id=pk)
        kutubxonachi.ism = reqest.POST['ismi']
        kutubxonachi.ish_vaqti = reqest.POST['i_vaqt']

        kutubxonachi.save()
        return redirect('/kutubxonachilar/')
    context = {
        'kutubxonachi': Kutubxonachi.objects.get(id=pk)
    }
    return render(reqest, 'kutubxonachi_tahrirlash.html', context)


def record_tahrirlash(reqest, pk):
    if reqest.method == "POST":
        record = Record.objects.get(id=pk)
        record.qaytarish_sana = reqest.POST['q_sana']
        record.qaytardi = reqest.POST.get('qaytardi')=='on'

        record.save()
        return redirect('/records/')
    context = {
        'recordlar': Record.objects.get(id=pk)
    }
    return render(reqest, 'record_tahrirlash.html', context)
