from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer, LoginSerializer

@api_view(['POST'])
def getData(req):
    serial = UserSerializer(data=req.data)
    if serial.is_valid():
        serial.save()
    print(serial.errors)
    return Response(serial.data)

@api_view(['POST'])
def getLogin(req):
    serial = LoginSerializer(data=req.data)
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

@api_view(['GET'])
def delete(req):
    user = User.objects.get(id=req.data['id'])
    user.delete()
    return Response("Ok")


from rest_framework import viewsets

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def batch_destroy(self, request):
        ids = request.data.get('ids', [])
        self.queryset.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)