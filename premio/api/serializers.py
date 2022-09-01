from rest_framework.serializers import ModelSerializer

from premio.models import Premio


class PremioSerializer(ModelSerializer):
    class Meta:
        model = Premio
        fields = "__all__"
