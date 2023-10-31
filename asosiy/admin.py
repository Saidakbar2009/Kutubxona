from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
# Register your models here.]
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'tugilgan_yil', 'tirik', 'jins', 'kitoblar_soni']
    list_display_links = ['id', 'ism']
    list_editable = ['tirik', 'kitoblar_soni']
    ordering = ['id']
    search_fields = ['ism', 'tugilgan_yil', 'id']
    search_help_text = "id, ism, tug'ilgan yili bo'yicha qidiring"
    list_filter = ['jins', 'tirik']
    list_per_page = 5
    date_hierarchy = 'tugilgan_yil'

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'sahifa', 'janr', "muallif"]
    search_fields = ['id', 'nom', 'muallif__ism']
    search_help_text = "id, nom va muallif bo'yicha qidirsa bo'ladi"
    list_filter = ['janr', 'muallif']
    ordering = ['nom']
    autocomplete_fields = ['muallif']

@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'ish_vaqti']
    search_fields = ['ism']
    search_help_text = 'ism boyicha qidiring'
    list_filter = ['ish_vaqti']


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['ism', 'kurs', 'kitoblar_soni']
    search_fields = ['ism']

@admin.register((Record))
class RecordAdmin(admin.ModelAdmin):
    list_display = ['talaba', 'kitob', 'kutubxonachi', 'olingan_sana', 'qaytarish_sana']
    autocomplete_fields = ['talaba', 'kitob', 'kutubxonachi']
# admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Kutubxonachi)
# admin.site.register(Record)

admin.site.unregister(Group)