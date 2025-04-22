from django.contrib import admin
from django.urls import path, include  # include를 추가
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pbl/', include('pbl.urls')),  # pbl 앱의 URL 연결
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)