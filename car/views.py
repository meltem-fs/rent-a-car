from rest_framework.viewsets import ModelViewSet

from .models import Car,Reservation
from .serializers import CarSerializer
from .permissions import IsStaffOrReadOnly

from django.db.models import Q

class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStaffOrReadOnly,)