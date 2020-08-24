# Generated by Django 3.1 on 2020-08-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('brand', models.CharField(max_length=30, verbose_name='Брэнд')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
