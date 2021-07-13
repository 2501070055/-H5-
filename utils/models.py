from django.db import models


class CommonModel(models.Model):
    """ 模型公共类 """
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateField('创建时间', auto_now_add=True)
    updated_at = models.DateField('修改时间', auto_now=True)

    class Meta:
        abstract = True



