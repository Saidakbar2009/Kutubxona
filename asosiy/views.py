from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def salomlash(request):
    return HttpResponse("Salom, Dunyo")

def bosh_sahifa(request):
    return render(request, "Home.html")

def kitoblar(request):
    s = Kitob.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        s = Kitob.objects.filter(nom__contains=soz) | Kitob.objects.filter(muallif__ism__contains=soz)
    data = {
        "books": s
    }
    return render(request, "Kitoblar.html", data)

def ayollar_kitoblari(request):
    k = Muallif.objects.filter(jins='Ayol')
    data = {
        "books": Kitob.objects.filter(muallif__in=k)
    }
    return render(request, 'mashq/ayollar.html', data)

def student(request):
    s = Talaba.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        s = Talaba.objects.filter(ism__contains=soz)
    data = {
        "books": s
    }
    return render(request, 'studentlar.html', data)

def books(request):
    m = Muallif.objects.filter(kitoblar_soni__lt=10)
    data = {
        "books": Kitob.objects.filter(muallif__in=m)
    }
    return render(request, 'mashq/Books.html', data)

def bitta_kitob(request, son):
    data = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, 'mashq/kniga.html', data)

# def kitoblar(request):
#     s = Kitob.objects.all()
#     soz = request.GET.get("qidiruv_sozi")
#     if soz is not None:
#         s = Kitob.objects.filter(nom__contains=soz) | Kitob.objects.filter(muallif__ism__contains=soz)
#     data = {
#         "books": s
#     }
#     return render(request, "Kitoblar.html", data)
def mualliflar(request):
    m = Muallif.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        m = Muallif.objects.filter(ism__contains=soz)
    data = {
        "books": m
    }
    return render(request, 'mashq/Mualliflar.html', data)

def tanlangan_muallif(request, son):
    data = {
        "books": Muallif.objects.get(id=son)
    }
    return render(request, 'mashq/Tanlangan.html', data)

def record(request):
    r = Record.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        r = Record.objects.filter(talaba__ism__contains=soz)
    data = {
        "books": r
    }
    return render(request, 'mashq/Recordlar.html', data)

def tirik(request):
    data = {
        "books": Muallif.objects.filter(tirik=True)
    }
    return render(request, 'mashq/Mualliflar.html', data)

def sahifa(request):
    data = {
        'books': Kitob.objects.order_by('-sahifa')[0:3]
    }
    return render(request, 'mashq/Sahifasikopkitob.html', data)

def kitob_soni(request):
    data = {
        'books': Muallif.objects.order_by('-kitoblar_soni')[0:3]
    }
    return render(request, 'mashq/Kitoblarsoni.html', data)

def record_sana(request):
    data = {
        'books': Record.objects.order_by('-olingan_sana')[0:3]
    }
    return render(request, 'mashq/Olish_sana.html', data)

def tirikning_kitobi(request):
    m = Muallif.objects.filter(tirik=True)
    data = {
        'books': Kitob.objects.filter(muallif__in=m)
    }
    return render(request, 'mashq/Tiriklar_kitobi.html', data)

def badiiy(request):
    data = {
        'books': Kitob.objects.filter(janr='Badiiy')
    }
    return render(request, 'mashq/badiiy.html', data)

def t_yil(request):
    data = {
        "books": Muallif.objects.order_by('-tugilgan_yil')[0:3]
    }
    return render(request, 'mashq/t_yil.html', data)

def bitta_record(request, son):
    data = {
        "kitob": Record.objects.get(id=son)
    }
    return render(request, 'mashq/Bitta_record.html', data)

def bitiruvchi(request):
    data = {
        "books": Talaba.objects.filter(kurs=4)
    }
    return render(request, 'mashq/Bitiruvchi.html', data)

def kitob_10(request):
    m = Muallif.objects.filter(kitoblar_soni__lt=10)
    data = {
        'books': Kitob.objects.filter(muallif__in=m)
    }
    return render(request, 'mashq/10kitob.html', data)

def talaba_ochir(request, son):
    Talaba.objects.filter(id=son).delete()
    return redirect("/student")

def kitob_ochir(request, son):
    Kitob.objects.filter(id=son).delete()
    return redirect("/kitob")

def muallif_ochir(request, son):
    Talaba.objects.filter(id=son).delete()
    return redirect("/muallif")