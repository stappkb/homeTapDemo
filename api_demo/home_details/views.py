from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import HomeDetails
from .serializers import HomeDetailsSerializer
from .services import HomeDetailsService

class HomeDetailsViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HomeDetails.objects.all()
    serializer = HomeDetailsSerializer()
    
    def list(self, request):
        details = HomeDetails.objects.all()
        serializer = HomeDetailsSerializer(details, many=True)
        return Response({"status": "success", "data": serializer.data})

    def create(self, request, pk=0):
        return Response('create')

    @action(detail=False, methods=['post'])
    def get_details(self, request):
        address = request.POST.get('address', None)
        postal_code = request.POST.get('postal_code', None)
        if not address:
            return Response(
                {"status": "required address not found."},
                status=status.HTTP_404_NOT_FOUND)
        if not postal_code:
            return Response(
                {"status": "required postal_code not found."},
                status=status.HTTP_404_NOT_FOUND)
        # check to make sure postal code is a int
        try:
            postal_code = int(postal_code)
        except Exception as e:
            return Response(
                {"status": "postal_code must be an int"},
                status=status.HTTP_404_NOT_FOUND)
        status, house_data = HomeDetailsService().get_house_data(address, postal_code)
        return Response({"status": status, "data": house_data})
