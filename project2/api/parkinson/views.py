from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from parkinson.models import parkinson
from parkinson.serializers import parkinsonSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def parkinson_list(request):

    if request.method == 'GET':
        parkinsons = parkinson.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            parkinsons = parkinsons.filter(title__icontains=title)
        
        parkinsons_serializer = parkinsonSerializer(parkinsons, many=True)
        return JsonResponse(parkinsons_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        parkinson_data = JSONParser().parse(request)
        parkinson_serializer = parkinsonSerializer(data=parkinson_data)
        if parkinson_serializer.is_valid():
            parkinson_serializer.save()
            return JsonResponse(parkinson_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(parkinson_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = parkinson.objects.all().delete()
        return JsonResponse({'message': '{} parkinsons were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def parkinson_detail(request, pk):
    try: 
        parkinson = parkinson.objects.get(pk=pk) 
    except parkinson.DoesNotExist: 
        return JsonResponse({'message': 'The parkinson does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        parkinson_serializer = parkinsonSerializer(parkinson) 
        return JsonResponse(parkinson_serializer.data) 
 
    elif request.method == 'PUT': 
        parkinson_data = JSONParser().parse(request) 
        parkinson_serializer = parkinsonSerializer(parkinson, data=parkinson_data) 
        if parkinson_serializer.is_valid(): 
            parkinson_serializer.save() 
            return JsonResponse(parkinson_serializer.data) 
        return JsonResponse(parkinson_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        parkinson.delete() 
        return JsonResponse({'message': 'parkinson was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def parkinson_list_published(request):
    parkinsons = parkinson.objects.filter(published=True)
        
    if request.method == 'GET': 
        parkinsons_serializer = parkinsonSerializer(parkinsons, many=True)
        return JsonResponse(parkinsons_serializer.data, safe=False)