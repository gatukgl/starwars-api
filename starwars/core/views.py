from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters

from core.models import People, Planet
from core.serializers import PeopleSerializer, PlanetSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'pk'


class PeopleGenericView(ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['gender']
    search_fields = ['name']


class PeopleInstanceView(RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'pk'


class PeopleListView(APIView):
    def get(self, request):
        peoples = People.objects.filter(gender='n/a')
        serializer = PeopleSerializer(peoples, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        homeworld = Planet.objects.first()

        serializer = PeopleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    lookup_field = 'pk'


class PlanetListView(ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetInstanceView(RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
