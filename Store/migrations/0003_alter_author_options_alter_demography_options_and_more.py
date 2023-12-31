# Generated by Django 4.2.4 on 2023-08-09 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_manga_description_alter_manga_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='demography',
            options={'verbose_name': 'Теги', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'verbose_name': 'Манга', 'verbose_name_plural': 'Манги'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='author_photos', verbose_name='Фото автора'),
        ),
        migrations.AlterField(
            model_name='demography',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно?'),
        ),
        migrations.AlterField(
            model_name='demography',
            name='demography',
            field=models.CharField(max_length=80, unique=True, verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно?'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=80, unique=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно?'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.CharField(max_length=555, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='image',
            field=models.ImageField(upload_to='обложка', verbose_name='Обложка манги'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название манги'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='original_name',
            field=models.CharField(max_length=255, verbose_name='Оригинальное название манги'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='recommended_age',
            field=models.CharField(max_length=30, verbose_name='Рекомендуемый возраст'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='year',
            field=models.CharField(max_length=6, verbose_name='Год'),
        ),
    ]
