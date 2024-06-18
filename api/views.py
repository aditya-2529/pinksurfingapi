from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer

@api_view(['POST'])
def getData(req):
    serial = UserSerializer(data=req.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

# @api_view(['POST'])
# def registerUser(req):
#     serial = RegisterSerializer(data=req.data)
#     if serial.is_valid():
#         serial.save()
#     return Response(serial.data)

@api_view(['GET'])
def add(req):
    user = User.objects.all()
    serial = UserSerializer(user,many=True)
    return Response(serial.data)

# @api_view(['DELETE'])
# def delete(req):
#     user = Login.objects.get(id=req.data['id'])
#     user.delete()
#     return Response("Ok")
