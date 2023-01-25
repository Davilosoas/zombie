from django.test import TestCase
from .models import Resource, Survivor

class SurvivorTestCase(TestCase):
    def test_create_survivor(self):
        resource = Resource.objects.create(name='water', point=10)
        survivor = Survivor.objects.create(name='John Doe', age=30, gender='M', latitude=1.23, longitude=4.56, infected=False)
        survivor.inventory.add(resource)
        survivor.save()
        print(resource.__dict__)
        print(survivor.__dict__)
        self.assertTrue(Survivor.objects.exists())
        self.assertTrue(Resource.objects.exists())
