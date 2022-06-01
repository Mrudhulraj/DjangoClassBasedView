from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CourseView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializers = CourseSerializer(courses, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=204)
        else:
            return Response(serializer.errors)


class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        courses = self.get_course(pk)
        serializers = CourseSerializer(courses)
        return Response(serializers.data)

    def delete(self, request, pk):
        courses = self.get_course(pk)
        courses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        courses = self.get_course(pk)
        serializers = CourseSerializer(courses, data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
