from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import People, Planet


class PeopleListView(APIView):
    def get(self, request):
        gender = request.query_params.get('gender', None)

        people_list = []
        if gender is not None:
            peoples = People.objects.filter(gender=gender)
        else:
            peoples = People.objects.all()

        for people in peoples:
            person = {
                'name': people.name,
                'gender': people.gender,
                'homeworld': people.homeworld.name
            }
            people_list.append(person)

        return Response(people_list)

    def post(self, request):
        data = request.data
        homeworld = Planet.objects.first()

        people = People.objects.create(
            name=data.get('name'),
            height=data.get('height'),
            mass=data.get('mass'),
            hair_color=data.get('hair_color'),
            skin_color=data.get('skin_color'),
            eye_color=data.get('eye_color'),
            birth_year=data.get('birth_year'),
            gender=data.get('gender'),
            homeworld=homeworld
        )

        person = {
            'name': people.name,
            'gender': people.gender,
            'homeworld': people.homeworld.name
        }

        return Response(person)
