from rest_framework import viewsets
from tapp.models import *
from tapp.serializers import *

class TModelListAPI(viewsets.ModelViewSet):
    queryset = TModel.objects.all()
    serializer_class = TModelSerializer
