from rest_framework import serializers

from core.models import People, Planet


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
