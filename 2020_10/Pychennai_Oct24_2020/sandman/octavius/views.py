
# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser

from octavius.serializers import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octavius.models import Snippet, Sleep
from octavius.serializers import SleepSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def sleep(request):
    if request.method == 'GET':
        sleep = Sleep.objects.all()
        serializer = SleepSerializer(sleep, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SleepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def sleep_update(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sleep = Sleep.objects.get(pk=pk)
    except Sleep.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SleepSerializer(sleep)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SleepSerializer(sleep, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sleep.delete()
        return HttpResponse(status=204)
