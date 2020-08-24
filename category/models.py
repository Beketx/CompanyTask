from django.db import models


class Category(models.Model):
    title = models.CharField("Название категории", max_length=30)
    description = models.TextField(default=' ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    title = models.CharField("Название под-категории", max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Под-Категория"
        verbose_name_plural = "Под-Категории"