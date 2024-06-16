from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Login
from .serializers import LoginSerializer

@api_view(['POST'])
def getLoginData(req):
    serial = LoginSerializer(data=req.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['GET'])
def add(req):
    user = Login.objects.all()
    serial = LoginSerializer(user,many=True)
    return Response(serial.data)

@api_view(['DELETE'])
def delete(req):
    user = Login.objects.get(id=req.data['id'])
    user.delete()
    return Response("Ok")
