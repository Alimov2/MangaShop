from django.db import models
from django.utils.text import slugify


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=80, unique=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    available = models.BooleanField(default=True, verbose_name="Доступно?")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genre)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.genre


class Demography(models.Model):
    demography = models.CharField(max_length=80, unique=True, verbose_name="Теги")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    available = models.BooleanField(default=True, verbose_name="Доступно?")

    class Meta:
        verbose_name = "Теги"
        verbose_name_plural = "Теги"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.demography)
        super(Demography, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.demography


class Author(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Имя автора"
    )
    photo = models.ImageField(
        upload_to="author_photos", blank=True, null=True, verbose_name="Фото автора"
    )
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Manga(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название манги")
    original_name = models.CharField(
        max_length=255, verbose_name="Оригинальное название манги"
    )
    description = models.CharField(max_length=555, verbose_name="описание")
    image = models.ImageField(upload_to="обложка", verbose_name="Обложка манги")
    year = models.CharField(max_length=6, verbose_name="Год")
    price = models.FloatField(blank=False, null=False, default=0, verbose_name="Цена")
    state = models.BooleanField(
        default=True, verbose_name="Состояние"
    )  
    country = models.CharField(max_length=50, verbose_name="Страна")
    recommended_age = models.CharField(max_length=30, verbose_name="Рекомендуемый возраст")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    genre = models.ManyToManyField(Genre)
    demography = models.ManyToManyField(Demography)
    available = models.BooleanField(default=True, verbose_name="Доступно?")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manga, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
