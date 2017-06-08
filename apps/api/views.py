###REST_FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from django.contrib.auth.models import User

@api_view(['GET'])
def test_users(request):
	if request.method =='GET':
		users=User.objects.all()
		serializer=UserSerializers(users,many=True)
		return Response(serializer.data)