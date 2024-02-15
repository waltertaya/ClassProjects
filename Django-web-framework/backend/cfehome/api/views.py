# from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
# import json
# from django.shortcuts import render
# from django.http import JsonResponse, HTTPResponse


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    '''
    api view for
    '''
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(instance, fields=['id', 'title',
        #                                          'content', 'price', 'sale_price'])
        # # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

    # return JsonResponse(data)
    return Response(data)


@api_view(["POST"])
def api_home2(request, *args, **kwargs):
    '''
    api view for
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
