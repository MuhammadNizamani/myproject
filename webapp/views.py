from rest_framework.views import APIView
from rest_framework.response import Response

from .models import employees
from .serializer import employeesSerializers


# Create your views here.

class employeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializers(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
