from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from .serializers import UserSerializer, ItemSerializer
from .models import Item
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cache_key = f'item_{item_id}'
        item = cache.get(cache_key)

        if not item:
            item = self.get_object()
            serializer = self.get_serializer(item)
            cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
            return Response(serializer.data)
        return Response(item)


