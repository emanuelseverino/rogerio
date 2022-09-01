from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import *
from rest_framework.mixins import *

from usuario.api.serializers import *

Usuario = get_user_model()


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.queryset.get(email=self.request.user.email)


'''
ViewSets que gerenciam as Empresas
'''


# Cria um novo usuário do tipo Empresa
class CriarEmpresaViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarEmpresaSerializer
    permission_classes = [IsAdminUser]


# Lista todos os usuários do tipo Empresa
class EmpresaViewSet(GenericViewSet, ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(tipo="EMPRESA")


'''
ViewSets que gerenciam os Espectadores
'''


class CriarEspecificadorViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarEspecificadorSerializer


class EspecificadorViewSet(GenericViewSet, ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = EspecificadorSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(tipo="ESPECIFICADOR")
