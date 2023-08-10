from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Search import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
    path('search/', include('Search.urls')),
    path('cart/', include('ShoppingCart.urls')),
    path('users/', include('AuthUsers.urls')),
    path('search-manga/', views.search_manga, name='buscar-manga'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)