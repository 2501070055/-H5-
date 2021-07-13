from django.contrib import admin

from system.models import Slider, ImageRelated
from utils.actions import set_valid, set_invalid


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    """ 景点基础信息 """
    list_display = ('name', 'desc', 'img', 'is_valid', 'created_at', 'updated_at', )
    search_fields = ('name', 'desc', )
    list_per_page = 20
    actions = [set_valid, set_invalid]


@admin.register(ImageRelated)
class ImageRelatedAdmin(admin.ModelAdmin):
    """ 景点基础信息 """
    list_display = ('summary', 'user', )
    list_per_page = 20
    actions = [set_valid, set_invalid]
