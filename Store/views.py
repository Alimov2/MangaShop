from django.shortcuts import render
from .models import Genre, Manga, Author, Demography
from django.core.paginator import Paginator


# Create your views here.
def store_manga(request):
    genres = Genre.objects.filter(available=True)
    mangas = Manga.objects.filter(available=True)
    demographies = Demography.objects.filter(available=True)

    paginator = Paginator(mangas, 6)
    page = request.GET.get("page")
    pages = paginator.get_page(page)

    return render(
        request,
        "store.html",
        {
            "genres": genres,
            #'mangas':mangas,
            "demographies": demographies,
            "mangas_pages": pages,
        },
    )


def detail_genre(request, slug):
    genre = Genre.objects.get(slug=slug)
    mangas = Manga.objects.filter(genre=genre)

    return render(
        request, "detail_genre_demography.html", {"genre": genre, "mangas": mangas}
    )


def detail_demographies(request, slug):
    demographies = Demography.objects.get(slug=slug)
    mangas = Manga.objects.filter(demography=demographies)

    return render(
        request,
        "detail_genre_demography.html",
        {"demographies": demographies, "mangas": mangas},
    )


def detail_authors(request, slug):
    authors = Author.objects.get(slug=slug)
    mangas = Manga.objects.filter(author=authors)

    return render(
        request, "detail_genre_demography.html", {"authors": authors, "mangas": mangas}
    )


def detail_manga(request, slug):
    manga = Manga.objects.get(slug=slug)

    return render(request, "detail_manga.html", {"manga": manga})


def full_image(request, slug):
    image = Manga.objects.get(slug=slug)

    return render(request, "full_image.html", {"image": image})
