from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LogSerializer, loginfo

# Create your views here.

@api_view(['GET'])
def show_data(request):
    log = loginfo.objects.all()
    serialize_log = LogSerializer(log, many=True)
    return Response(serialize_log.data)

@api_view(['GET'])
def user_data(request, id):
    log = loginfo.objects.filter(unique_code = id).all()
    serialize_log = LogSerializer(log, many=True)
    return Response(serialize_log.data)
