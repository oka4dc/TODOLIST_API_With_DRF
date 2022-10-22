from pickle import GET
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API_App.models import items
from My_API.serializers import ItemsSerializer

@api_view(['GET'])
def GetData(request):
    #person = ['Dennis', 'Okafor', 23]
    #person = {"Name": "Dennis", "Age": 24}
    item=items.objects.all()
    serializer=ItemsSerializer(item, many=True)
    return Response(serializer.data)