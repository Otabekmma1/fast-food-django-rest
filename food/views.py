from rest_framework.viewsets import *
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from .models import *

class FoodTypeApiList(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class FoodApiList(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class CommentApiList(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

