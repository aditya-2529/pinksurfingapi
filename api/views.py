from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Users
from .serializers import UserSerializer

@api_view(['GET'])
def getData(req):
    user = Users.objects.all()
    serial = UserSerializer(user, many=True)
    return Response(serial.data)

@api_view(['POST'])
def add(req):
    serial = UserSerializer(data=req.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)
