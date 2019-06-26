from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
import json
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Songs,EntryValues
from .serializers import SongsSerializer,DataSerializer




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    result = {}


    runRequestBody = {'script':'console.log(7+5)',
                  'language': 'nodejs',
                  'versionIndex': '1',
                  'clientId': settings.APP_ID,
                  'clientSecret' :  settings.APP_KEY}
    headers = {'Content-type': 'application/json'}

    response = requests.post('https://api.jdoodle.com/execute',data=json.dumps(runRequestBody),headers=headers)
    return HttpResponse(response)
    print(response.json())





class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

# Create your views here.


class ListCreateDataView(generics.ListCreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = EntryValues.objects.all()
    serializer_class = DataSerializer



    def post(self, request, *args, **kwargs):



        a_data = EntryValues.objects.create(
            script=request.data["script"],
            language=request.data["language"],
            versionIndex=request.data["versionIndex"],

        )
        runRequestBody = {'script': request.data.get("script"),
                          'language': request.data.get("language"),
                          'versionIndex': request.data.get("versionIndex"),
                          'clientId': settings.APP_ID,
                          'clientSecret': settings.APP_KEY}
        headers = {'Content-type': 'application/json'}

        response = requests.post('https://api.jdoodle.com/execute', data=json.dumps(runRequestBody), headers=headers)
        return Response(
            data=response.json(),
            status=status.HTTP_201_CREATED
        )


class ListDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = EntryValues.objects.all()

    runRequestBody = {'script': 'console.log(7+5)',
                      'language': 'nodejs',
                      'versionIndex': '1',
                      'clientId': settings.APP_ID,
                      'clientSecret': settings.APP_KEY}
    headers = {'Content-type': 'application/json'}

    response = requests.post('https://api.jdoodle.com/execute', data=runRequestBody, headers=headers)
    serializer_class = DataSerializer