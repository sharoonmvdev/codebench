from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from student.serializers import SignUpSerializer

class StudentCreateView(CreateAPIView):

    serializer_class = SignUpSerializer

    
