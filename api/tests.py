from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs,EntryValues
from .serializers import SongsSerializer,DataSerializer
from django.conf import settings
import json

import requests

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        # add test data
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Songs.objects.all()
        print(expected)
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.



class GetAllDataTest():

    def test_get_all_data(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint

        response = self.client.get(
            reverse("data-all", kwargs={"version": "v1"})
        )
        # fetch the data from db


        runRequestBody = {'script': 'console.log(7+5)',
                          'language': 'nodejs',
                          'versionIndex': '1',
                          'clientId': settings.APP_ID,
                          'clientSecret': settings.APP_KEY}
        headers = {'Content-type': 'application/json'}
        responsegot = requests.post('https://api.jdoodle.com/execute', data=json.dumps(runRequestBody), headers=headers)
        expected = responsegot
        serialized = DataSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
