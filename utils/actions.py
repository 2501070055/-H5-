from django.contrib import messages


def set_invalid(modelAdmin, request, queryset):
    queryset.update(is_valid=False)
    messages.success(request, '操作成功')


def set_valid(modelAdmin, request, queryset):
    queryset.update(is_valid=True)
    messages.success(request, '操作成功')


set_invalid.short_description = '禁用'
set_valid.short_description = '启用'
