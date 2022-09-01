from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from premio.api.viewsets import PremioViewSet
from usuario.api.viewsets import UsuarioViewSet, CriarEmpresaViewSet, CriarEspecificadorViewSet, EspecificadorViewSet, \
    EmpresaViewSet

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'cadastro/empresa', CriarEmpresaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'cadastro/especificador', CriarEspecificadorViewSet)
router.register(r'especificador', EspecificadorViewSet)
router.register(r'premio', PremioViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('login/', obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
