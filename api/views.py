from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Login
from .serializers import LoginSerializer

@api_view(['POST'])
def getLoginData(req):
    user = Login.objects.all()
    serial = LoginSerializer(user, many=True)
    return Response(serial.data)

@api_view(['POST'])
def add(req):
    serial = LoginSerializer(data=req.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['DELETE'])
def dele(req):
    user = Login.objects.get(id=req.data['id'])
    serial = LoginSerializer(data=req.data)
    if serial.is_valid():
        user.delete()
    return Response(serial.data)
