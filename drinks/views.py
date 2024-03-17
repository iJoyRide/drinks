from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Drink
from .serializers import DrinksSerializer


@api_view(["GET", "POST"])
def drink_list(request):

    # get all the drinks
    # serialize them
    # return json
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinksSerializer(drinks, many=True)

        return JsonResponse({"drinks": serializer.data})

    if request.method == "POST":
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "POST", "DELETE"])
def drink_detail(request, id):
    
    try:
        Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    