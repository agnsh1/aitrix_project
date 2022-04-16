from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ads(BaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Наименование товара'
    )
    added_at = models.DateField(verbose_name='добавлено', blank=True,
                                )
    price = models.CharField(
        max_length=255,
        null=False, blank=False,
        verbose_name='Цена'
    )
    description = models.TextField(
        max_length=3000,
        verbose_name='Описание товара'
    )
    main_image = models.ImageField(
        upload_to='images',
        verbose_name='Главное фото',
        null=True, blank=True
    )
    subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        verbose_name = 'Объевление'
        verbose_name_plural = 'Объевлений'

    def __str__(self):
        return f' {self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='название категории')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='подкатегория')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='категория',
        related_name='ads_subcategory'
    )

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return self.title


class AdsImages(BaseModel):
    images = models.ImageField(upload_to='images', verbose_name='Картинки')
    ads = models.ForeignKey(
        Ads,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='ads_images'
    )
