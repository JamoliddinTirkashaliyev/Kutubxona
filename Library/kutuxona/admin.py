

from django.contrib import admin
from django.contrib.auth.models import User, Group


from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display=["id","ism","kurs","kitoblar_soni"]
    list_display_links = ['ism']
    list_editable = ['kurs','kitoblar_soni']
    list_filter = ["kurs"]
    search_fields = ['ism','id']
    search_help_text = 'Id va Ism boyicha qidiring!'
    list_per_page = 2

class MuallifAdmin(admin.ModelAdmin):
    list_display=["id","ism","jins","tugilgan_sana","tirik","kitoblar_soni"]
    list_display_links = ['ism']
    list_editable = ['kitoblar_soni']
    search_fields = ['ism','id','tugilgan_sana']
    list_filter = ['tirik']
    date_hierarchy = 'tugilgan_sana'

class KitobAdmin(admin.ModelAdmin):
    list_display=["id","nom","muallif","sahifa","janr"]
    list_display_links = ['nom']
    list_editable = ['sahifa']
    search_fields = ['nom','id','muallif__ism']
    autocomplete_fields = ['muallif']


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob, KitobAdmin)
admin.site.register(Kutubxonachi)
admin.site.register(Record)
