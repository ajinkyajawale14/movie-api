#django imports
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#rest_framework imports
from rest_framework import routers

#views imports
from movies import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
#router.register(r'genres', views.GenreViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
