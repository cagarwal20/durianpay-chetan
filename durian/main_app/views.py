from django.shortcuts import render
from .models import Product 
from .serializers import ProductSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .helper import flipkart_scrape,snapdeal_scrape,paytmmall_scrape,nykaa_scrape,westside_scrape
# Create your views here.

import requests
from bs4 import BeautifulSoup
 

@api_view(['GET'])
def get_data(request):
    search = request.GET.get('search')
    ordering_by = request.GET.get('ordering_by','price')
    limit = request.GET.get('limit',3)
    websites = request.GET.get('websites',None)
    if websites:
        website_list = websites.strip('][').split(',')
        objects = Product.objects.filter(url__icontains=search,website__in=website_list).order_by(ordering_by)[:int(limit)]

    else:
        objects = Product.objects.filter(url__icontains=search).order_by(ordering_by)[:int(limit)]

    if objects.count()>0:
        ser_data = ProductSerializer(objects,many=True)
        return Response({"products":ser_data.data,"total_products_considered":objects.count()},status=200)
    else:
        try:
            flipkart_scrape(search)
        except Exception as e:
            return Response({"error":str(e)},status=400)
        try:
            snapdeal_scrape(search)
        except Exception as e:
            return Response({"error":str(e)},status=400)
        try:
            paytmmall_scrape(search)
        except Exception as e:
            return Response({"error":str(e)},status=400)
        try:
            nykaa_scrape(search)
        except Exception as e:
            return Response({"error":str(e)},status=400)
        try:
            westside_scrape(search)
        except Exception as e:
            return Response({"error":str(e)},status=400)
        return Response({"data":"updated, reload again to see the result"},status=200)






