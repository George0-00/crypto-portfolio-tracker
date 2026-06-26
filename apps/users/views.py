from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer


@api_view(['POST'])
def register(request):
    serializers = RegisterSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
        return Response({
            'message': 'User created successfuly'
        }, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
