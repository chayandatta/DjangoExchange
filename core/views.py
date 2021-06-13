from datetime import datetime
from typing import Dict, Any, Union

import requests_cache
import requests
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from ratelimit.decorators import ratelimit
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DjangoExchangeApi
from .models import ExchangeModel
from bunch import bunchify

requests_cache.install_cache('django_exchange_cache', backend='sqlite', expire_after=180)


@ratelimit(key='ip', rate='5/m')
@ratelimit(key='ip', rate='100/d')
@api_view(['GET', 'POST'])
def django_xchange(request):
    """

    :rtype: object
    """
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 404,
            'message': 'This method is not available'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        try:

            url = 'https://api.stackexchange.com/2.2/search/advanced'
            payload = {"page": request.POST['page'],
                       "pagesize": request.POST['pagesize'],
                       "fromdate": request.POST['fromdate'],
                       "todate": request.POST['todate'],
                       "min": request.POST['min'],
                       "max": request.POST['max'],
                       "order": request.POST['order'],
                       "sort": request.POST['sort'],
                       "q": request.POST['q'],
                       "accepted": request.POST['accepted'],
                       "answers": request.POST['answers'],
                       "body": request.POST['body'],
                       "closed": request.POST['closed'],
                       "migrated": request.POST['migrated'],
                       "notice": request.POST['notice'],
                       "nottagged": request.POST['nottagged'],
                       "tagged": request.POST['tagged'],
                       "title": request.POST['title'],
                       "user": request.POST['user'],
                       "url": request.POST['url'],
                       "views": request.POST['views'],
                       "wiki": request.POST['wiki'],
                       "site": "stackoverflow",
                       }
            print(payload)
            resp = requests.get(url, data=payload)
            print(resp)

            print("At Time: {0} / Used Cache: {1}".format(datetime.now(), resp.from_cache))

            if resp.status_code != 200:
                if resp.status_code == 404:
                    return JsonResponse({
                        'statusCode': 404,
                        'message': 'No info found'
                    }, status=status.HTTP_404_NOT_FOUND)
                else:
                    return JsonResponse({
                        'statusCode': 500,
                        'message': 'StackExchange is down'
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                try:
                    save_data(request)
                    data = resp.json()
                    return JsonResponse({
                        'statusCode': 200,
                        'data': data
                    }, status=status.HTTP_200_OK)
                except json.decoder.JSONDecodeError as e:
                    return JsonResponse({
                        'statusCode': 500,
                        'message': str(e)
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return JsonResponse(data={
                'statusCode': 500,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def save_data(request):
    exchange_obj = ExchangeModel(
        page_no=request.POST['page'],
        page_size=request.POST['pagesize'],
        from_date=request.POST['fromdate'],
        to_date=request.POST['todate'],
        order_by=request.POST['order'],
        min_date=request.POST['min'],
        max_date=request.POST['max'],
        sort_by=request.POST['sort'],
        question=request.POST['q'],
        is_accepted=request.POST['accepted'],
        no_of_answers=request.POST['answers'],
        body=request.POST['body'],
        is_closed=request.POST['closed'],
        is_migrated=request.POST['migrated'],
        notice=request.POST['notice'],
        not_tagged=request.POST['nottagged'],
        tagged=request.POST['tagged'],
        title=request.POST['title'],
        user=request.POST['user'],
        url=request.POST['url'],
        views=request.POST['views'],
        wiki=request.POST['wiki'])

    exchange_obj.save()

