from pickle import GET
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def GetData(request):
    #person = ['Dennis', 'Okafor', 23]
    person = {"Name": "Dennis", "Age": 24}
    return Response(person)