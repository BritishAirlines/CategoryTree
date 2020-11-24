from rest_framework.views import APIView
from django.http import Http404
from .models import Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryReportSerializer, NestedCategorySerializer


class CategoriesView(APIView):

    def post(self, request):
        serializer = NestedCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategoryReportSerializer(category)
        return Response(serializer.data)
