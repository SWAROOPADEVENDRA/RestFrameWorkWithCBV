from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from app.models import *

from app.serializers import *

class ProductCrud(APIView):
    def get(selff,request):
        LSO=Product.objects.all()
        MSDO=ProductModelserializers(LSO,many=True)

        return Response(MSDO.data)
    def post(self,request):
        RJSO=request.data
        PSO=ProductModelserializers(data=RJSO)
        if PSO.is_valid():
            PSO.save()
            return Response({'msg':'data insert successfuully'})
        else:
            return Response({'failed':'invalid data'})