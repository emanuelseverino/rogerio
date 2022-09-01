from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import *

from premio.api.serializers import PremioSerializer
from premio.models import Premio


class PremioViewSet(GenericViewSet, ListAPIView):
    queryset = Premio.objects.all()
    serializer_class = PremioSerializer
    permission_classes = [IsAuthenticated, ]
