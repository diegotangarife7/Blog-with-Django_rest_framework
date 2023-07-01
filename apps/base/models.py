from django.db import models


class BaseModel(models.Model):
    # id
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True