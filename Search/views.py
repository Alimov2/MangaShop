from django.shortcuts import render
from django.contrib import messages
from Store.models import Manga, Author, Genre, Demography
# Create your views here.
def search_manga(request):

    if request.GET['search']: 

        text = request.GET['search'] 
        
        if len(text) < 3:
            messages.error(request, 'Введенный текст слишком короткий. Попробуйте еще раз...')

            return render(request, 'results_search.html')

        else: 
            results = Manga.objects.filter(name__icontains=text) 

            return render(request, 'results_search.html', {
                    'results':results, 
                    'query':text.title(),})

    else: 
        messages.error(request, 'Пустой поиск... 💀')

        return render(request, 'results_search.html')



# def search_author(request):
#     davailables_demographies = Demography.objects.filter(available=True)
#     availables_genres = Genre.objects.filter(available=True) 

#     if request.GET['search']:

#         text = request.GET['search']
#         if len(text) < 3:
#             messages.error(request, 'Введенный текст слишком короткий. Попробуйте еще раз...')

#             return render(request, 'начинать')

#         else:
#             results = Author.objects.filter(name__icontains=text)

#         return render(request, 'results_search.html', {
#             'results':results, 
#             'query':results,
#             'davailables_demographies':davailables_demographies,
#             'availables_genres':availables_genres})
#     else:
#         messages.error(request, 'Нет результатов')

#         return render(request, 'начинать')

# def search_genre(request):
#     davailables_demographies = Demography.objects.filter(available=True)
#     availables_genres = Genre.objects.filter(available=True) 

#     if request.GET['search']:

#         text = request.GET['search']
#         if len(text) < 3:
#             messages.error(request, 'Введенный текст слишком короткий. Попробуйте еще раз...')

#             return render(request, 'начинать')

#         else:
#             results = Genre.objects.filter(genre__icontains=text)

#         return render(request, 'results_search.html', {
#             'results':results, 
#             'query':results,
#             'davailables_demographies':davailables_demographies,
#             'availables_genres':availables_genres})
#     else:
#         messages.error(request, 'Нет результатов')

#         return render(request, 'НАЧАТЬ')

# def search_demography(request):
#     davailables_demographies = Demography.objects.filter(available=True)
#     availables_genres = Genre.objects.filter(available=True) 

#     if request.GET['search']:

#         text = request.GET['search']
#         if len(text) < 3:
#             messages.error(request, 'Введенный текст слишком короткий. Попробуйте еще раз...')

#             return render(request, 'НАЧАТЬ')

#         else:
#             results = Demography.objects.filter(demography__icontains=text)

#         return render(request, 'results_search.html', {
#             'results':results, 
#             'query':results,
#             'davailables_demographies':davailables_demographies,
#             'availables_genres':availables_genres})
#     else:
#         messages.error(request, 'Нет результатов')

#         return render(request, 'НАЧАТЬ')
