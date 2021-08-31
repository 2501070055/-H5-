from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.forms import ProfileForm
from accounts.models import Profile, User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """ 用户基础管理 """
    list_display = ('username', 'nickname', 'is_active', 'is_staff', 'date_joined', )
    search_fields = ('username', 'nickname', )
    # 新增的表单
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname', )}),
    )
    # 修改的表单
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname', 'avatar', )}),
    )

    actions = ['disable_user', 'enable_user']

    def disable_user(self, request, queryset):
        queryset.update(is_active=False)

    def enable_user(self, request, queryset):
        queryset.update(is_active=True)

    disable_user.short_description = '禁用'
    enable_user.short_description = '启用'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ 用户详细信息表 """
    list_display = ('format_username', 'sex', 'age', 'created_at', )
    list_per_page = 3
    list_select_related = ('user', )
    list_filter = ('sex', )
    search_fields = ('username', 'user__nickname', )
    fields = ('real_name', 'email', 'phone_no', 'sex', 'age', )
    # 表单验证
    form = ProfileForm

    def format_username(self, obj):
        """ 用户名脱敏处理
        :param obj: Profile
        :return:
        """
        return obj.username[:3] + '*****' + obj.username[3:-1]

    # 修改列名称
    format_username.short_description = '用户名'
