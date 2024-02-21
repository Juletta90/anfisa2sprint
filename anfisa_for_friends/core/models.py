from django.db import models


# При наследовании от абстрактных моделей verbose_name поля надо
# указывать в абстрактной модели. В проекте anfisa_for_friends поле
# is_published вынесено в абстрактную модель PublishedModel, так что
# переводить его нужно в описании этой модели.

class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        abstract = True
