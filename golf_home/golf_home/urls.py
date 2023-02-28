from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from golf_home import settings
from store.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('auth/', include('authorization.urls')),
]

# Когда Debug = True
if settings.DEBUG:
    # к уже сущ. маршрутам добавляем еще для статических данных
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Обработка страницы - 404
handler404 = page_not_found
