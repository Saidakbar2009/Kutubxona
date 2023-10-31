from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def salomlash(request):
    return HttpResponse("Salom, Dunyo")

def bosh_sahifa(request):
    return render(request, "Home.html")

def kitoblar(request):
    forma = KitobForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
        # Kitob.objects.create(
        #     nom = request.POST.get("nomi"),
        #     sahifa = request.POST.get("k_s"),
        #     janr = request.POST.get("janr"),
        #     muallif = Muallif.objects.get(id=request.POST.get("m"))
        # )
        return redirect('/kitob/')
    s = Kitob.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        s = Kitob.objects.filter(nom__contains=soz) | Kitob.objects.filter(muallif__ism__contains=soz)
    data = {
        "books": s,
        "muallif": Muallif.objects.all(),
        "forma": KitobForm
    }
    return render(request, "Kitoblar.html", data)

def ayollar_kitoblari(request):
    k = Muallif.objects.filter(jins='Ayol')
    data = {
        "books": Kitob.objects.filter(muallif__in=k)
    }
    return render(request, 'mashq/ayollar.html', data)

def student(request):
    if request.method == 'POST':
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get("i"),
                kurs = forma.cleaned_data.get("k"),
                kitoblar_soni = forma.cleaned_data.get("k_s")
            )
        # Talaba.objects.create(
        #     ism = request.POST.get("ismi"),
        #     kurs = request.POST.get("kurs"),
        #     kitoblar_soni = request.POST.get("k_son")
        # )
        return redirect('/student/')
    s = Talaba.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        s = Talaba.objects.filter(ism__contains=soz)
    data = {
        "books": s,
        "forma": TalabaForm()
    }
    return render(request, 'studentlar.html', data)

def books(request):
    m = Muallif.objects.filter(kitoblar_soni__lt=10)
    data = {
        "books": Kitob.objects.filter(muallif__in=m),
    }
    return render(request, 'mashq/Books.html', data)

def bitta_kitob(request, son):
    data = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, 'mashq/kniga.html', data)
def mualliflar(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Muallif.objects.create(
        #     ism = request.POST.get("ismi"),
        #     tugilgan_yil = request.POST.get("t_y"),
        #     jins = request.POST.get("jinsi"),
        #     kitoblar_soni = request.POST.get("k_s"),
        #     tirik = request.POST.get("t") == "on"
        # )
        return redirect('/muallif/')
    m = Muallif.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        m = Muallif.objects.filter(ism__contains=soz)
    data = {
        "books": m,
        "forma": MuallifForm()
    }
    return render(request, 'mashq/Mualliflar.html', data)

def tanlangan_muallif(request, son):
    data = {
        "books": Muallif.objects.get(id=son)
    }
    return render(request, 'mashq/Tanlangan.html', data)

def record(request):
    forma = RecordForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
        # Record.objects.create(
        #     talaba = Talaba.objects.get(id=request.POST.get("talaba")),
        #     kitob = Kitob.objects.get(id=request.POST.get("kitob")),
        #     kutubxonachi = Kutubxonachi.objects.get(id=request.POST.get("kutubxonachi")),
        #     olingan_sana = request.POST.get("sana")
        # )
        return redirect('/record/')
    r = Record.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        r = Record.objects.filter(talaba__ism__contains=soz)
    data = {
        "books": r,
        "talaba": Talaba.objects.all(),
        "kitob": Kitob.objects.all(),
        "kutubxonachi": Kutubxonachi.objects.all(),
        "forma": RecordForm
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
    Muallif.objects.filter(id=son).delete()
    return redirect("/muallif/")

def record_ochir(request, son):
    Record.objects.filter(id=son).delete()
    return redirect('/record/')

def talaba_update(request, pk):
    if request.method == 'POST':
        x = Talaba.objects.get(id=pk)
        x.ism = request.POST.get("ismi")
        x.kurs = request.POST.get("kurs")
        x.kitoblar_soni = request.POST.get("k_son")
        x.save()
        return redirect('/student/')
    data = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(request, 'talaba_update.html', data)

def kitob_update(request, id):
    if request.method == 'POST':    
        x = Kitob.objects.get(id=id)
        x.nom = request.POST.get("nomi")
        x.janr = request.POST.get("janr")
        x.sahifa = request.POST.get("k_s")
        x.muallif = Muallif.objects.get(id=request.POST.get("m"))
        x.save()
        return redirect('/kitob/')
    data = {
        "books": Kitob.objects.get(id=id),
        "muallif": Muallif.objects.all(),
        "janrlar": ["Badiiy", "Ilmiy", "Hujjatli"]
    }
    return render(request, 'Kitob_ozgartir.html', data)

def kutubxonachi(request):
    forma = KutubxonachiForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            Kutubxonachi.objects.create(
                ism = forms.cleaned_data.get("i"),
                ish_vaqti = forms.cleaned_data.get("ish")
            )
        # Kutubxonachi.objects.create(
        #     ism = request.POST.get("ism"),
        #     ish_vaqti = request.POST.get("vaqt")
        # )
        return redirect('/kutubxonachi/')
    data = {
        "kutubxonachi": Kutubxonachi.objects.all(),
        "forma": KutubxonachiForm()
    }
    return render(request, 'Kutubxonachi.html', data)


def muallif_update(request, id):
    if request.method == 'POST':
        x = Muallif.objects.get(id=id)
        x.ism = request.POST.get("ismi")
        x.jins = request.POST.get("jinsi")
        x.kitoblar_soni = request.POST.get("k_s")
        x.save()
        return redirect('/muallif/')
    data = {
        "muallif": Muallif.objects.get(id=id),
        "jins": ['Erkak', 'Ayol']
    }
    return render(request, 'muallif_update.html', data)
def kutubxonachi_update(request, id):
    if request.method == 'POST':
        x = Kutubxonachi.objects.get(id=id)
        x.ism = request.POST.get('ism')
        x.ish_vaqti = request.POST.get('vaqt')
        x.save()
        return redirect('/kutubxonachi/')
    data = {
        "kutubxonachi": Kutubxonachi.objects.all()
    }
    return render(request, 'kutubxonachi_update.html', data)

def record_update(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == 'POST':
        record.olingan_sana = request.POST.get("sana")
        record.qaytarish_sana = request.POST.get("sana1")
        record.save()
        return redirect('/record/')
    data = {
        "record": record
    }
    return render(request, 'record_update.html', data)


