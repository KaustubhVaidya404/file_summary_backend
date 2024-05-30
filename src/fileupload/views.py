from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFilesSerializer
import pandas as pd 


# Create your views here.


@api_view(['POST'])
def upload_file(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    obj = request.FILES['file']
    serializerobj = UploadedFilesSerializer(data=request.data)
    if serializerobj.is_valid():
        serializerobj.save()
        file_ext = obj.name.split('.')[-1]
        if file_ext == 'csv':
            return Response(serializerobj.data, status=status.HTTP_201_CREATED)
        elif file_ext in ['xlsx', 'xls']:
            return Response(serializerobj.data, status=status.HTTP_201_CREATED)   
        else:
            return Response(serializerobj.errors, status=status.HTTP_400_BAD_REQUEST)  
    return Response(serializerobj.errors, status=status.HTTP_400_BAD_REQUEST)