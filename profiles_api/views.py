from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView freatures"""
        
        an_apiview = [
           'User HTTP method as funcion (get,post,patch,put,delete)', 
            'Is similar to a tradicional django view',"most control",
            'Is mapped manually to URLs'
        ]
    
        return Response({'message' : 'Hello!','an_apiview':an_apiview})