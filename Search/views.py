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
