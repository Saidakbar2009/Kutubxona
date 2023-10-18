from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', bosh_sahifa),
    path('kitob/', kitoblar),
    path('ayollar/', ayollar_kitoblari),
    path('student/', student),
    path('book/', books),
    path('bitta_kitob/<int:son>/', bitta_kitob),
    path('bitta_record/<int:son>/', bitta_record),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('tanlangan_muallif/<int:son>/', tanlangan_muallif),
    path('muallif/', mualliflar),
    path('tirik/', tirik),
    path('sahifasi/', sahifa),
    path('record/', record),
    path('kitob_soni/', kitob_soni),
    path('record_sana/', record_sana),
    path('tirikning_kitobi/', tirikning_kitobi),
    path('badiiy/', badiiy),
    path('t_yil/', t_yil),
    path('bitiruvchi/', bitiruvchi),
    path('10kitob/', kitob_10),
]
