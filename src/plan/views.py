from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WorkVolumeSerializer
from .services import WorkVolumeService


class WorkVolumeView(APIView):

    def post(self, request):
        serializer = WorkVolumeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errorCode': 279, 'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        work_volume_service = WorkVolumeService(request.user, serializer.validated_data)

        response_data = work_volume_service.process()
        status_code = response_data.pop('status')

        return Response(data=response_data, status=status_code)
