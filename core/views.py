from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def django_xchange(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 404,
            'message': 'This method is not available'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        try:
            pass
        except Exception as e:
            raise Http404
