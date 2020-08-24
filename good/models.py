from django.db import models
from category.models import SubCategory


class Good(models.Model):
    title = models.CharField("Название", max_length=30)
    photo = models.ImageField("Изображение", upload_to='images/')
    price = models.IntegerField("Цена", default=0)
    size = models.IntegerField("Размер")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.CharField("Брэнд", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
